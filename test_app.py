import os
import requests
from app import app


def test_version():
    response = requests.get('http://localhost:5000/version')
    assert response.status_code == 200
    assert response.json() == {'version': 'v0.0.1'}


def test_metrics():
    response = requests.get('http://localhost:5000/metrics')
    assert response.status_code == 200


def test_temperature():
    os.environ['SENSEBOX_IDS'] = (
        '5eba5fbad46fb8001b799786,'
        '5eba5fbad46fb8001b799787,'
        '5eba5fbad46fb8001b799788'
    )
    with app.test_client() as client:
        response = client.get('/temperature')
        assert response.status_code == 200
        data = response.json()
        assert 'average_temperature' in data
        assert 'status' in data
