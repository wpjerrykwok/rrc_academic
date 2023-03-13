# COMP2040 Python Essentials With Data Analysis
# Assignment 7: Robo-Trumps
# Wai Ping KWOK
# read data from a file to create robot trump cards
# Created on 2023 02 04
# Sample output:
# Available robots
# rainbow
# space
# bird
# dog
# jet
# round
# brains
# twoheads
# shades
# hair
# tv
# yellow
# Choose a robot (pick a name, or random):
# [display in Python Turtle Graphics]

# import libraries
from turtle import *
from random import choice

# setup turtle screen
screen = Screen()
screen.bgcolor("white")
penup()
hideturtle()

# setup dictionary to store the robots
robots = {}

# open external file
file = open("cards.txt", "r")

# read robot info into dictionary
for line in file.read().splitlines():
  name, battery, intelligence, speed, strength, font_color, image = line.split(', ')
  robots[name] = [battery, intelligence, speed, strength, font_color, image]
  screen.register_shape(image)

# close the file
file.close()

# user to choose a robot
while True:
  print("Available robots")
  for key in robots:
    print(key)
  
  robot = input("Choose a robot (pick a name, or random, or exit to quit the game): ")

  # choose a random robot
  if robot == "random":
    robot = choice(list(robots.keys()))
  # display the robot
  if robot in robots:
    stats = robots[robot]
    style = ("MS Sans Serif", 14, "bold")
    clear()
    goto(0, 100)
    shape(stats[5])
    setheading(90)
    stamp()
    setheading(-90)
    forward(80)
    color(stats[4])
    write("Name: " + robot, font = style, align = "center")
    forward(30)
    write("Battery: " + stats[0], font = style, align = "center")
    forward(30)
    write("Intelligence: " + stats[1], font = style, align = "center")
    forward(30)
    write("Speed: " + stats[2], font = style, align = "center")
    forward(30)
    write("Strength: " + stats[3], font = style, align = "center")
  # to exit the game
  elif robot == "exit":
    bye()
    break
  else:
    print("Robot doesn\'t exist!")
