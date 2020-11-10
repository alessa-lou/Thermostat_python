class Thermostat():

    def __init__(self, temp = 20):
        self.temperature = temp
        self.MIN_TEMP = 10

    def get_current_temp(self):
        return self.temperature
    
    def up(self):
        self.temperature += 1
    
    def down(self):
        if self.is_min_temp() == True:
            return self.MIN_TEMP
        else:
            self.temperature -= 1

    def is_min_temp(self):
        if self.temperature == self.MIN_TEMP:
          return True
