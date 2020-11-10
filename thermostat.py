class Thermostat():

    def __init__(self, temp = 20):
        self.temperature = temp
        self.MIN_TEMP = 10
        self.power_saving_mode = True

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

    def is_PSM_on(self):
        if self.power_saving_mode == True:
            return True
        else:
            return False

    def switch_PSM_off(self):
        self.power_saving_mode = False

    def switch_PSM_on(self):
        self.power_saving_mode = True