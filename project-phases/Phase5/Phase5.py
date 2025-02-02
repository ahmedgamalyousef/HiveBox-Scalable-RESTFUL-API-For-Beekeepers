import os
from flask import Flask, jsonify, Response
from prometheus_client import start_http_server, Gauge, generate_latest
import redis
from minio import Minio
from datetime import datetime
from prometheus_client import start_http_server, Counter
import time
import threading

app = Flask(__name__)
version = " v0.0.1 "
# Set SENSEBOX_ID from environment variable
SENSEBOX_ID = "5eba5fbad46fb8001b799786"
sensebox_id = os.getenv("SENSEBOX_ID")
if sensebox_id is None:
    raise ValueError("SENSEBOX_ID environment variable is not set")

# Prometheus metrics
app_metric = Gauge('app_metric', 'Description')


# Version endpoint
@app.get("/version")
def get_version():
    return {"version": version}


# Temperature endpoint
@app.get("/temperature")
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
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


# function to get temperature reading
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
