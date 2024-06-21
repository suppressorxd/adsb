from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aircraft')
def get_aircraft_data():
    url = "https://opensky-network.org/api/states/all"
    params = {
        'lamin': -90,     
        'lamax': 90,     
        'lomin': -180,    
        'lomax': 180    
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()['states'][:300]   
        aircraft_info = []
        for aircraft in data:
            icao24 = aircraft[0]
            latitude = aircraft[6]
            longitude = aircraft[5]
            altitude = aircraft[7]
            velocity = aircraft[9]
            callsign = aircraft[1]   
            aircraft_info.append({
                'Uçağı takip etmek için gerekli kod': icao24,
                'latitude': latitude,
                'longitude': longitude,
                'altitude': altitude,
                'velocity': velocity,
                'callsign': callsign
            })
        return jsonify(aircraft_info)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
