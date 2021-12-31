# define a class using namedtuple
from collections import namedtuple
Car = namedtuple("Car", "color mileage")

my_car = Car("red", 3182.4)
my_car.color #red
my_car.mileage #3812.4
my_car #Car(color='red' , mileage=3812.4)

# like tuples, namedtuples are immutable
my_car.color = "blue" #AttributeError: can't set attribute
