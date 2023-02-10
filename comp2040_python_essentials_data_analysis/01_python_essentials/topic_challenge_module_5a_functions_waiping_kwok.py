# COMP2040 Python Essentials With Data Analysis
# Topic Challenge - Module 5A - Functions
# Wai Ping KWOK
#
# Write a function that returns the max
# when given a list of numbers as an argument.
# Write a function that calculates the standard deviation
# when given a list of numbers as an argument.
#
# Created on 2023 02 01
# Sample output:
# We have the list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The maximum is: 10
# The mean is: 5.5
# The standard deviation is: 2.8722813232690143

# import libraries
import math


def find_max(get_list: list) -> float:
    """
    return the max, when given a list of numbers as an argument\n
    args:
        get_list (list): the list of numbers from which a maximum
        to be obtained
    returns:
        max_in_list (float): the maximum number in the list
    """
    max_in_list = get_list[0]
    for count in range(len(get_list)):
        if max_in_list < get_list[count]:
            max_in_list = get_list[count]
    return max_in_list


def find_mean(get_list: list) -> float:
    """
    return the mean, when given a list of numbers as an argument\n
    args:
        get_list (list): the list of numbers from which a mean
        to be obtained
    returns:
        mean_of_list (float): the mean of the list
    """
    total = 0
    for count in range(len(get_list)):
        total += get_list[count]

    mean_of_list = total / len(get_list)

    return mean_of_list


def find_dev(get_list: list) -> float:
    """
    return the standard deviation, when given a list of numbers
    as an argument\n
    args:
        get_list (list): the list of numbers from which a standard deviation
        to be obtained
    returns:
        dev_of_list (float): the standard deviation of the list
    """
    total_for_stdev = 0
    mean = find_mean(get_list)
    for count in range(len(get_list)):
        total_for_stdev += (get_list[count] - mean) ** 2

    stdev_of_list = math.sqrt(total_for_stdev / len(get_list))

    return stdev_of_list


# specify the list of numbers
list_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# display the results
print('We have the list:')
print(list_to_check)
print('The maximum is:', find_max(list_to_check))
print('The mean is:', find_mean(list_to_check))
print('The standard deviation is:', find_dev(list_to_check))
