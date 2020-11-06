import pytest
from thermostat import Thermostat


def test_temperature():
    thermostat = Thermostat()
    assert thermostat.temperature() == 20