import os
from flask import Flask, jsonify, Response
from prometheus_client import start_http_server, Gauge, generate_latest

app = Flask(__name__)

# Set SENSEBOX_ID from environment variable
sensebox_id = os.getenv("SENSEBOX_ID")
if sensebox_id is None:
    raise ValueError("SENSEBOX_ID environment variable is not set")

# Prometheus metrics
app_metric = Gauge('app_metric', 'Description')


# Temperature endpoint
@app.route('/temperature', methods=['GET'])
def temperature():
    temp = get_temperature_reading()
    if temp < 10:
        status = "Too Cold"
    elif 11 <= temp <= 36:
        status = "Good"
    else:
        status = "Too Hot"
    return jsonify({"temperature": temp, "status": status})


# Metrics endpoint
@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


# Example function to get temperature reading (replace with actual implementation)
def get_temperature_reading():
    return 25  # Placeholder value

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)


# Basic integration test example
def test_temperature_endpoint():
    response = app.test_client().get('/temperature')
    assert response.status_code == 200


def test_metrics_endpoint():
    response = app.test_client().get('/metrics')
    assert response.status_code == 200

# Run tests
if __name__ == '__main__':
    test_temperature_endpoint()
    test_metrics_endpoint()
