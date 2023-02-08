# COMP2040 Python Essentials With Data Analysis
# Module 3A - Basic Data Types
# Assignment 2: Password Generator
# Author: Wai Ping KWOK
# Created on 2023 01 09

# import the library for use
import random

# define the characters to be used in the password
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+<>,.?'

# user inputs for the number of passwords and
# the length of the password to be generated
number = int(input('number of passwords? '))
length = int(input('password length? '))

for p in range(number):   # looping for number of passwords
    password = ""
    # looping for length of passwords
    for c in range(length):
        # random a character from the defined chars
        password += random.choice(chars)
    print(password)
