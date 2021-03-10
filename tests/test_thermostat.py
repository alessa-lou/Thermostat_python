import pytest
from thermostat import Thermostat

@pytest.fixture
def thermostat():
    thermostat = Thermostat()
    return thermostat

def test_initial_temperature(thermostat):
    assert thermostat.temperature == 20

def test_increase_temperature(thermostat):
    thermostat.up()
    assert thermostat.get_current_temp() == 21

def test_decrease_temperature(thermostat):
    thermostat.down()
    assert thermostat.get_current_temp() == 19

def test_min_temp(thermostat):
    for i in range(11):
        thermostat.down()
    assert thermostat.get_current_temp() == 10

def test_PSM_default_on(thermostat):
    assert thermostat.is_PSM_on() == True

def test_switch_PSM_off(thermostat):
    thermostat.switch_PSM_off()
    assert thermostat.is_PSM_on() == False

def test_switch_PSM_on(thermostat):
    thermostat.switch_PSM_off()
    assert thermostat.is_PSM_on() == False
    thermostat.switch_PSM_on()
    assert thermostat.is_PSM_on() == True

def test_PSM_on_limit(thermostat):
    for i in range(6):
        thermostat.up()
    assert thermostat.get_current_temp() == 25

def test_PSM_off_limit(thermostat):
    thermostat.switch_PSM_off()
    for i in range(13):
        thermostat.up()
    assert thermostat.get_current_temp() == 32

def test_reset_temp(thermostat):
    for i in range(6):
        thermostat.up()
    thermostat.reset_temp()
    assert thermostat.get_current_temp() == 20

def test_low_energy_usage(thermostat):
    for i in range(3):
        thermostat.down()
    assert thermostat.energy_usage() == "low-usage"

def test_medium_energy_usage(thermostat):
    assert thermostat.energy_usage() == "medium-usage"

def test_high_energy_usage(thermostat):
    thermostat.switch_PSM_off()
    for i in range(6):
        thermostat.up()
    assert thermostat.energy_usage() == "high-usage"
