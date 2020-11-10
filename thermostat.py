class Thermostat():

    def __init__(self, temp = 20):
        self.temperature = temp

    def get_current_temp(self):
        return self.temperature
    
    def up(self):
        self.temperature += 1
    
    def down(self):
        self.temperature -= 1
