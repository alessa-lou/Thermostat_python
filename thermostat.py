class Thermostat():        
    instance = None
    _init_called = False

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Thermostat, cls).__new__(cls)
            cls.instance.__initialized = False
        return cls.instance


    def __init__(self):
        if Thermostat._init_called:
            print(True)
        Thermostat._init_called = True
        print("INIT")
        self.DEFAULT_TEMP = 20
        self.temperature = self.DEFAULT_TEMP
        self.MIN_TEMP = 10
        self.MAX_TEMP_PSM_ON = 25
        self.MAX_TEMP_PSM_OFF = 32
        self.power_saving_mode = True
        self.MEDIUM_ENERGY_USAGE_LIMIT = 18
        self.HIGH_ENERGY_USAGE_LIMIT = 25
    
    # def instance(cls):
    #     if cls._instance is None:
    #         print("Creating the object")
    #         cls._instance = super(Thermostat, cls).__new__(cls)
    #         return cls._instance
    #     else:
    #         return cls.__init__

    def get_current_temp(self):
        return self.temperature
    
    def up(self):
        if self.is_max_temp_in_PSM() == True:
            return self.MAX_TEMP_PSM_ON
        elif self.is_max_temp_in_PSM() == False:
            return self.MAX_TEMP_PSM_ON
        else:
            self.temperature += 1
    
    def down(self):
        if self.is_min_temp() == True:
            return self.MIN_TEMP
        else:
            self.temperature -= 1

    def is_min_temp(self):
        if self.temperature == self.MIN_TEMP:
          return True

    def is_max_temp_in_PSM(self):
        if self.is_PSM_on() == True and self.temperature == self.MAX_TEMP_PSM_ON:
            return True
        elif self.is_PSM_on() == False and self.temperature == self.MAX_TEMP_PSM_OFF:
            return False

    def is_PSM_on(self):
        if self.power_saving_mode == True:
            return True
        else:
            return False

    def switch_PSM_off(self):
        self.power_saving_mode = False

    def switch_PSM_on(self):
        self.power_saving_mode = True

    def reset_temp(self):
        self.temperature = self.DEFAULT_TEMP

    def energy_usage(self):
        if self.temperature < self.MEDIUM_ENERGY_USAGE_LIMIT:
            return "Low usage"
        elif self.temperature <= self.HIGH_ENERGY_USAGE_LIMIT:
            return "Medium usage"
        else:
            return "High usage"
