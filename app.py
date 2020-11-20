from flask import Flask, render_template, url_for, request, redirect
from thermostat import Thermostat

import json
from flask import jsonify

app = Flask(__name__)
thermostat = Thermostat()

@app.route('/')
def index():
    # print(request.json)
    return render_template('index.html')

@app.route('/temperature', methods=["GET"])
def temp():
    print(thermostat)
    print("Get sent")
    list = {
        "temperature": thermostat.temperature,
        "power_save_mode_on": thermostat.is_PSM_on(),
        "energy_usage": thermostat.energy_usage(),
        "status": 200
    }    
    json_data = json.dumps(list)
    return json_data

@app.route('/temperature', methods=["POST"])
def temp_post():
    print(request.form)
    obj = request.form.to_dict()
    new_thing = json.dumps(obj)
    print(new_thing)
    
    if "up" in new_thing:
        print("hello youre in the up")
        thermostat.up()
        print(thermostat.temperature)
        return jsonify(status=200)
    elif "down" in new_thing:
        print("hello youre in the down")
        thermostat.down()
        print(thermostat.temperature)
        return jsonify(status=200)
    elif "reset" in new_thing:
        print("hello youre in the reset")
        thermostat.reset_temp()
        print(thermostat.temperature)
        return jsonify(status=200)
    else:
        return print("hello this went a bit wrong")

@app.route('/power-saving-mode', methods=["POST"])
def power_saving():
    obj = request.form.to_dict()
    new_thing = json.dumps(obj)
    if "on" in new_thing:
        print("you are in psm on")
        thermostat.switch_PSM_on()
        return jsonify(status=200)
    else:
        print("you are in psm off")
        thermostat.switch_PSM_off()
        return jsonify(status=200)

if __name__ == '__main__':
    app.run()