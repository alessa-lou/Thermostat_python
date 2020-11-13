from flask import Flask, render_template, url_for, request, redirect
from thermostat import Thermostat

import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # print(request.json)
    return render_template('index.html')

@app.route('/temperature', methods=["GET"])
def temp():
    thermostat = Thermostat()
    print(thermostat.temperature)
    # print(request.json)
    print("Bonjour")
    list = {
        "temperature": thermostat.temperature,
        "power_saving_mode": thermostat.is_PSM_on(),
        "energy_usage": thermostat.energy_usage(),
        "status": 200
    }    
    return jsonify(results = list)

@app.route('/temperature', methods=["POST"])
def temp_post():
    thermostat = Thermostat()
    print(request.get_json())
    print(request.args.get("#temperature-up"))
    if request.args.get("temperature-up"):
        return thermostat.up()
    elif request.args.get("temperature-down"):
        return thermostat.down()
    elif request.args.get("temperature-reset"):
        return thermostat.reset_temp()
    else:
        return "?"
    # jsonify(status=200)

@app.route('/power-saving-mode', methods=["POST"])
def power_saving():
    thermostat = Thermostat()
    print(request.args.get("power-saving-on"))
    if request.args.get("power-saving-on"):
        return thermostat.switch_PSM_on
    else:
        return thermostat.switch_PSM_off

if __name__ == '__main__':
    app.run()