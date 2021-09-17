# Object Oriented Programming
#   splitting up larger tasks into smaller pieces
#   each of those pieces can become reusable

# Objects
#   things that make up an object: attributes(variables) and methods(functions)
#   you can generate multiples of the same object, which we call a Class
#   a Class blueprint creates an individual Object

# Creating a New Object
#   car = CarBlueprint()
#   the object is 'car', the class is CarBlueprint, with () activating construction

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink4")
# timmy.forward(100)

# Object Attributes
#   car.speed => calls on that attribute
#   car is object, speed is attribute

# my_screen = Screen()
# print(my_screen.canvheight)

# Object Methods
#   car.stop() => calls on method
#   car is object, stop is method

# my_screen.exitonclick()

# Python Packages: a bunch of code that other people have written
#   pypi.org - Python Package Index
#   install package by going to PyCharm - Preferences - Name of File - Python Interpreter - Search for package

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
