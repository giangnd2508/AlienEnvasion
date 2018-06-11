class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.tank = 100

    def get_descriptive_name(self):
        print(self.make, self.model, self.year)

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, tank):
        print("This car a gas tank " + str(self.tank))


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        if self.battery_size in range(70, 85):
            range_km = 240
        elif self.battery_size >= 85:
            range_km = 270

        msg = "This car can go approximately " + str(range_km) + " miles on a full charge."
        print(msg)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, tank):
        print("Electric car has no tank")


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
