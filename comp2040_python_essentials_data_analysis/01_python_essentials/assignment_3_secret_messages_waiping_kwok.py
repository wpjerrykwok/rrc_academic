# COMP2040 Python Essentials With Data Analysis
# Assignment 3: Secret Messages
# Wai Ping KWOK
# Create an encrption program to send and receive secret messages
# Created on 2023 01 10
# Sample output:
# Please enter the key: -4
# Please enter a message: Hello world!
# Your new message is Hahhk sknhz!

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# user input for the key
key = int(input('Please enter the key: '))

new_message = ''

# user input for the message to encrypt
message = input('Please enter a message: ')

# loop for each character in message
for character in message:
    # condition if character is in alphabet
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character

# display the encrypted message
print('Your new message is', new_message)
