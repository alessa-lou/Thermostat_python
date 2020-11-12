from flask import Flask, render_template, url_for, request, redirect
from thermostat import Thermostat

import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature')
def temp():
    thermostat = Thermostat()
    list = {
        "temperature": thermostat.temperature,
        "power_saving_mode": thermostat.is_PSM_on(),
        "energy_usage": thermostat.energy_usage(),
        "status": 200

    }    
    return jsonify(results = list)

@app.route('/temperature', methods=['POST'])
def post():
    thermostat = Thermostat()
    if "up":
        return thermostat.up()
    elif "down":
        return thermostat.down()
    elif "reset":
        return thermostat.reset_temp()
    else:
        return "?"
    jsonify(status=200)
    

if __name__ == '__main__':
    app.run()