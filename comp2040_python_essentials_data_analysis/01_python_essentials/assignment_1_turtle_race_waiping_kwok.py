# COMP2040 Python Essentials With Data Analysis
# Module 2C - Using the IDLE3 IDE
# Assignment 1: Turtle Race
# Author: Wai Ping KWOK
# Created on 2023 01 09

# import the libraries for use
from turtle import *
from random import randint

# set the drawing speed
speed(100)

# set the starting position
penup()
goto(-140, 140)

for step in range(15):    # looping to draw the vertical lines
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    for dash in range(10):  # looping to draw the dashes
        forward(10)
        penup()
        forward(10)
        pendown()
    penup()
    backward(210)
    left(90)
    forward(20)

# create the first turtle
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
    ada.right(36)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(10):
    bob.left(36)

carl = Turtle()
carl.color('green')
carl.shape('turtle')

carl.penup()
carl.goto(-160, 40)
carl.pendown()

for turn in range(10):
    carl.right(36)

dan = Turtle()
dan.color('purple')
dan.shape('turtle')

dan.penup()
dan.goto(-160, 10)
dan.pendown()

for turn in range(10):
    dan.left(36)

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    carl.forward(randint(1, 5))
    dan.forward(randint(1, 5))
