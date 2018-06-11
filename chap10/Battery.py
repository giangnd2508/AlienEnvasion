class Battery():
    def __int__(self):
        self.battery_size = 100

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery")


my_bat = Battery()
my_bat.describe_battery()
