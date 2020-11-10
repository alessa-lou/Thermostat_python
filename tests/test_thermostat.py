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