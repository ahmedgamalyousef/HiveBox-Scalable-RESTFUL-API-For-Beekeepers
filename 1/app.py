from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version': 'v0.0.1'})

@app.route('/temperature', methods=['GET'])
def temperature():
    senseBox_ids = ['5eba5fbad46fb8001b799787']
    temperatures = []
    for senseBox_id in senseBox_ids:
        response = requests.get(f'https://api.opensensemap.org/boxes/{senseBox_id}')
        if response.status_code == 200:
            data = response.json()
            print(f"Data for senseBox ID {senseBox_id}: {data}")  # Print the entire data structure

            # Check if 'sensors' key exists and print debugging information
            if 'sensors' in data:
                print(f"'sensors' key found in data for senseBox ID {senseBox_id}")
                if len(data['sensors']) > 0:
                    try:
                        temperature = float(data['sensors'][0]['lastMeasurement']['value'])
                        temperatures.append(temperature)
                    except KeyError as e:
                        print(f"KeyError for senseBox ID {senseBox_id}: {e}")
                else:
                    print(f"No sensors found for senseBox ID {senseBox_id}")
            else:
                print(f"'sensors' key not found in data for senseBox ID {senseBox_id}")
        else:
            print(f"Failed to fetch data for senseBox ID {senseBox_id} with status code {response.status_code}")
    avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0
    return jsonify({'average_temperature': avg_temp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
