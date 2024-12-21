import requests
from datetime import datetime, timedelta, timezone
from prometheus_client import generate_latest, Gauge, Summary
import redis
from minio import Minio
from apscheduler.schedulers.background import BackgroundScheduler
import io
from flask import Flask, jsonify

app = Flask(__name__)

# Prometheus metrics
TEMPERATURE_GAUGE = Gauge(
    'average_temperature',
    'Average temperature of senseBox sensors'
)
request_time = Summary(
    'request_processing_seconds',
    'Time spent processing request'
)

# Set senseBox IDs directly in the code
senseBox_ids = ['5eba5fbad46fb8001b799786']

# Initialize Redis client
try:
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_client.ping()
    print("Connected to Redis")
except redis.ConnectionError as e:
    print(f"Redis connection error: {e}")
    exit(1)

# Initialize MinIO client
minio_client = Minio(
   'minio:9000', access_key='minioadmin', secret_key='minioadmin', secure=False
)


# Function to store data in MinIO
def store_data():
    print("Starting data storage...")
    for senseBox_id in senseBox_ids:
        data = redis_client.get(senseBox_id)
        if data:
            print(
                f"Storing data for senseBox ID {senseBox_id}: "
                f"{data.decode('utf-8')}"
            )  # Debug print
            data_stream = io.BytesIO(data)  # Wrap bytes in a BytesIO object
            try:
                minio_client.put_object(
                    'mybucket', f"{senseBox_id}.json", data_stream,
                    length=len(data), content_type='application/json'
                )
                print(
                    f"Successfully stored data for senseBox ID "
                    f"{senseBox_id}"
                )
            except Exception as e:
                print(f"Failed to store data for senseBox ID{senseBox_id}:{e}")
        else:
            print(f"No data found in Redis for senseBox ID {senseBox_id}")


# Scheduler to store data every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(store_data, 'interval', minutes=5)
scheduler.start()


# Function to cache temperature data in Redis
def cache_temperature(senseBox_id, temperature):
    print(
        f"Caching temperature for senseBox ID {senseBox_id}: {temperature}"
    )  # Debug print
    result = redis_client.set(
        # Cache for 5 minutes
        senseBox_id, temperature, ex=300
    )
    # Debug print
    print(f"Cache result for senseBox ID {senseBox_id}: {result}")


@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version': 'v0.0.1'})


@app.route('/metrics', methods=['GET'])
@request_time.time()
def metrics():
    return generate_latest()


@app.route('/temperature', methods=['GET'])
def temperature():
    temperatures = []
    current_time = datetime.now(timezone.utc)

    for senseBox_id in senseBox_ids:
        cached_temp = redis_client.get(senseBox_id)
        if cached_temp:
            print(
                f"Found cached temperature for senseBox ID {senseBox_id}: "
                f"{cached_temp.decode('utf-8')}"
            )  # Debug print
            temperatures.append(float(cached_temp))
            continue

        try:
            response = requests.get(
                f'https://api.opensensemap.org/boxes/{senseBox_id}',
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            print(
                f"Data for senseBox ID {senseBox_id}: {data}"
            )  # Debug print

            temperature_sensor = next((
                sensor for sensor in data['sensors']
                if sensor['title'].lower() == 'temperatur'
            ), None)
            if temperature_sensor:
                last_measurement = temperature_sensor.get('lastMeasurement')
                print(
                    f"Last measurement for senseBox ID {senseBox_id}: "
                    f"{last_measurement}"
                )  # Debug print
                if last_measurement and 'createdAt' in last_measurement:
                    measurement_time = datetime.strptime(
                        last_measurement['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ'
                    ).replace(tzinfo=timezone.utc)
                    # Adjusted recent threshold
                    if current_time - measurement_time < timedelta(days=2):
                        temperature = float(last_measurement['value'])
                        print(
                         f"Fetched temperature for senseBox ID {senseBox_id}: "
                         f"{temperature}"
                        )  # Debug print
                        temperatures.append(temperature)
                        cache_temperature(senseBox_id, temperature)
                    else:
                        print(
                         f"No recent measurement for senseBox ID {senseBox_id}"
                        )
                else:
                    print(
                     f"No createdAt field in last measurement for senseBox ID "
                     f"{senseBox_id}")

            else:
                print(
                 f"No temperature sensor found for senseBox ID " 
                 f"{senseBox_id}")
        except requests.exceptions.RequestException as e:
            print(
                f"Failed to fetch data for senseBox ID {senseBox_id}: {e}"
            )

    avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0
    print(f"Calculated average temperature: {avg_temp}")  # Debug print
    TEMPERATURE_GAUGE.set(avg_temp)
    status = (
        'Too Cold' if avg_temp < 10 else (
            'Good' if avg_temp <= 36 else 'Too Hot'
        )
    )

    return jsonify(
        {'average_temperature': avg_temp, 'status': status}
    )


@app.route('/store', methods=['POST'])
def store():
    store_data()
    return jsonify({'status': 'Data stored successfully'})


@app.route('/readyz', methods=['GET'])
def readyz():
    inaccessible_count = sum(
        1 for senseBox_id in senseBox_ids if not redis_client.get(senseBox_id)
    )
    if inaccessible_count <= len(senseBox_ids) // 2 and all(
        redis_client.ttl(senseBox_id) > 0 for senseBox_id in senseBox_ids
    ):
        return jsonify({'status': 'Ready'}), 200
    return jsonify({'status': 'Not Ready'}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
