from car2 import ElectricCar as EC

my_leaf = EC('nissan','leaf', 2024)
print("전기차는 {}".format(my_leaf.get_descriptiove_name()))

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

