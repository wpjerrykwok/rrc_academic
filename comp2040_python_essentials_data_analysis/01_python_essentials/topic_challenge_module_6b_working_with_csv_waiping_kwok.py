# COMP2040 Python Essentials With Data Analysis
# Topic Challenge - Module 6B - Working With CSV Files
# Wai Ping KWOK
# Create functions to read a csv file into dictionary,
# calculate an average, display all original data and
# the calculated average
# Created on 2023 02 07
# sample .csv input:
# "Temp","Press","Humidity"
# 1.1,55.5,22.2
# 3.3,4.4,6.6
# 8.8,99.9,7.7
# sample on-screen output:
# original data:
# Temp, Press, Humidity
# 1.1, 55.5, 22.2
# 3.3, 4.4, 6.6
# 8.8, 99.9, 7.7
# Average Temp : 4.4

# import library for use
import csv


def read_and_avg(csv_file_name: str, item_to_avg: str) -> float:
    """
    read the csv file into dictionary and calculate an average\n
    args:
        csv_file_name (str): the name of the csv file
        item_to_avg (str): the name of the item to calculate
        the mean
    returns:
        avg (float): the calculated average of the item
    """
    with open(csv_file_name, mode="r", newline="") as mydata:
        csv_reader = csv.DictReader(mydata, delimiter=",")
        total = 0
        count = 0
        for line in csv_reader:
            for key, value in line.items():
                if key == item_to_avg:
                    total += float(value)
                    count += 1
    avg = total/count
    return avg


def show_data(csv_file_name: str):
    """
    print out the original data in a csv file\n
    args:
        csv_file_name (str): the name of the csv file
    returns:
        empty
    """
    with open(csv_file_name, mode="r", newline="") as mydata:
        csvreader = csv.reader(mydata, delimiter=",")
        for line in csvreader:
            print(", ".join(line))


csv_file_name = "topic_challenge_module_6b_weather.csv"
item_to_avg = "Temp"

print("original data:")
show_data(csv_file_name)
print("Average", item_to_avg, ":", read_and_avg(csv_file_name, item_to_avg))
