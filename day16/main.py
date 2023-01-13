# #one way to do it:

# #import turtle

# #timmy =  turtle.Turtle()

# #another way to do it
# from turtle import Turtle, Screen
# import prettytable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("CornflowerBlue")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)