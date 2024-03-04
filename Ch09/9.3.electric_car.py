class Car:
    """ A class that represents a car """
    def __init__(self, make, model, year):
        """Initializing car properties"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a clear and clean name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the rangefinder to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increases the rangefinder value by a given value"""
        self.odometer_reading += miles

class Battery:
    """A class that represents the battery of an electric vehicle"""
    def __init__(self, battery_size = 40):
        """Initialize the battery's properties."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a sentence describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """It tells you how far you can drive with this battery."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Define features specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initializes the properties of the parent class """
        """And initialize the properties specific to electric vehicles."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Prints a sentence describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars do not have fuel tanks"""
        print("This car doesn't have a gas tank!")



my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()