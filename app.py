from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta
from prometheus_client import generate_latest, Gauge


app = Flask(__name__)

TEMPERATURE_GAUGE = Gauge(
    'average_temperature',
    'Average temperature of senseBox sensors'
)


@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version': 'v0.0.1'})


@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest()


@app.route('/temperature', methods=['GET'])
def temperature():
    senseBox_ids = [
        '5eba5fbad46fb8001b799786',
        '5eba5fbad46fb8001b799787',
        '5eba5fbad46fb8001b799788'
    ]  # Add more IDs as needed

    temperatures = []
    current_time = datetime.utcnow()

    for senseBox_id in senseBox_ids:
        response = requests.get(f'https://api.opensensemap.org/boxes/{senseBox_id}')
        if response.status_code == 200:
            data = response.json()
            if 'sensors' in data and len(data['sensors']) > 0:
                try:
                    last_measurement = data['sensors'][0]['lastMeasurement']
                    measurement_time = datetime.strptime(
                        last_measurement['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ'
                    )
                    if current_time - measurement_time < timedelta(hours=1):
                        temperature = float(last_measurement['value'])
                        temperatures.append(temperature)
                except (KeyError, ValueError) as e:
                    print(f"Error for senseBox ID {senseBox_id}: {e}")
        else:
            print(
                f"Failed to fetch data for senseBox ID {senseBox_id} "
                f"with status code {response.status_code}"
            )

    avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0
    TEMPERATURE_GAUGE.set(avg_temp)
    status = 'Too Cold' if avg_temp < 10 else 'Good' if avg_temp <= 36 else 'Too Hot'

    return jsonify({'average_temperature': avg_temp, 'status': status})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
