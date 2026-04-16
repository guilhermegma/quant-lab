from sensor import Sensor

class SensorFinanceiro(Sensor):
    def __init__ (self, name, unit_of_measurement, frequency, currency) :
        super().__init__(name, unit_of_measurement, frequency)
        self.currency = currency

