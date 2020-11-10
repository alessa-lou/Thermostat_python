import pytest
from thermostat import Thermostat


def test_initial_temperature():
    thermostat = Thermostat()
    assert thermostat.temperature == 20

def test_increase_temperature():
    thermostat = Thermostat()
    thermostat.up()
    assert thermostat.get_current_temp() == 21

def test_decrease_temperature():
    thermostat = Thermostat()
    thermostat.down()
    assert thermostat.get_current_temp() == 19

def test_min_temp():
    thermostat = Thermostat()
    for i in range(11):
      thermostat.down()
    assert thermostat.get_current_temp() == 10

def test_PSM_default_on():
    thermostat = Thermostat()
    assert thermostat.power_saving_mode == True

def test_switch_PSM_off():
    thermostat = Thermostat()
    thermostat.switch_PSM_off()
    assert thermostat.is_PSM_on() == False

def test_switch_PSM_on():
    thermostat = Thermostat()
    thermostat.switch_PSM_off()
    assert thermostat.is_PSM_on() == False
    thermostat.switch_PSM_on()
    assert thermostat.is_PSM_on() == True