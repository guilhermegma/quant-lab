from sensor import Sensor

class FinancialSensor(Sensor):
    def __init__ (self, name, unit_of_measurement, frequencies, currency) :
        super().__init__(name, unit_of_measurement, frequencies)
        self.currency = currency

    def resume (self):
        print(f"{self.name} | {self.currency} | {self.frequencies} | Readings: {len(self.readings)}")
    
class HealthSensor(Sensor):
    def __init__ (self, name, unit_of_measurement, frequencies, patient) :
        super().__init__(name, unit_of_measurement, frequencies)
        self.patient = patient

    def resume (self):
        print(f"{self.name} | Patient: {self.patient} | frequencies: {self.frequencies} | Readings: {self.readings}")

def main():
    financial_sensor = FinancialSensor('EUR/USD', 'USD', 10, 'USD')
    health_sensor = HealthSensor('Cardiac', 'bpm', 1, 'João Silva')

    financial_sensor.add_value(32)
    financial_sensor.add_value(56)
    financial_sensor.add_value(78)

    health_sensor.add_value(90)

    financial_sensor.resume()
    financial_sensor.print_list()

    health_sensor.resume()
    health_sensor.print_list()
if __name__ == '__main__':
    main()