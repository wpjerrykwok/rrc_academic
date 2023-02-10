# COMP2040 Python Essentials With Data Analysis
# Assignment 8: Where is the Space Station
# Wai Ping KWOK
# use a web service to find out the current location of
# the International Space Station (ISS) and
# plot its location on a map.
# Created on 2023 02 09
# Sample output:
# People in Space:  10
# Sergey Prokopyev in ISS
# Dmitry Petelin in ISS
# Frank Rubio in ISS
# Nicole Mann in ISS
# Josh Cassada in ISS
# Koichi Wakata in ISS
# Anna Kikina in ISS
# Fei Junlong in Shenzhou 15
# Deng Qingming in Shenzhou 15
# Zhang Lu in Shenzhou 15
# Latitude:  43.2618
# Longitude:  -101.1558
# [see screen of a map and a logo with text output]

# import libraries
import json
import turtle
import urllib.request

# use web service to find out who is currently in space
# http://open-notify.org/Open-Notify-API/
url_astro = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url_astro)

astros = json.loads(response.read())
print("People in Space: ", astros["number"])

# print out the name and the craft
people = astros["people"]
crafts = {}
for p in people:
    print(p["name"], "in", p["craft"])
    if p["craft"] not in crafts.keys():
        crafts[p["craft"]] = (p["name"])
    else:
        crafts[p["craft"]] += "\n" + p["name"]

# use web service to find out where the International Space Station is
url_iss = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url_iss)
iss_now = json.loads(response.read())

location = iss_now["iss_position"]
lat = float(location["latitude"])
lon = float(location["longitude"])
print("Latitude: ", lat)
print("Longitude: ", lon)

# show the position of ISS on a map
# image source:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("assignment_8_map.png")

screen.register_shape("assignment_8_iss.gif")

iss = turtle.Turtle()
iss.shape("assignment_8_iss.gif")
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# output on screen
space_ship_people = turtle.Turtle()
space_ship_people.penup()
space_ship_people.hideturtle()

space_ship_people.color("white")
space_ship_people.goto(-175, 20)
space_ship_people.write("people in space: " + str(astros["number"]))

count = 0
for key, value in crafts.items():
    space_ship_people.goto(-175 + 60 * count, -60)
    space_ship_people.write("spaceship:\n" + str(key) + "\n\n" + str(value))
    count += 1

screen.exitonclick()
