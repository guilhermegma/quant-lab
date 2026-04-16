class Sensor:
    def __init__(self, name, unit_of_measurement, frequencies):
        self.name = name
        self.unitOfMeasurement = unit_of_measurement
        self.frequencies = frequencies
        self.readings = []

    def add_value (self, value):
        self.readings.append (value)

    def print_list (self):
        print(f"Reading values are: {self.readings}")

def main():
    
    Sensor1 = Sensor('RadioFrequency', 'GHz', 24)
    Sensor2 = Sensor('Radar', 'GHz', 300)

    Sensor1.add_value(32)
    Sensor1.add_value(56)
    Sensor1.add_value(78)

    Sensor2.add_value(90)

    Sensor1.print_list()
    Sensor2.print_list()

if __name__ == '__main__':
    main()