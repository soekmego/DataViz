"""
Data Visualization Project

Parse data from an CSV or Excel File, render in GeoJSON
save to a database and visualize in graph form

This project is for educational purposes.
"""

from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "../data/sammple_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parse a raw CSV file to JSON-like object."""
    
    #Open CSV file
    open_file = open(raw_file)
    
    #Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    #Setup empty list
    parsed_data = []

    #Skip headers in first line of the CSV file
    fields = csv_data.next()

    #Iterate over each row of CSV file, zip together with field keys
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #Close CSV file
    opened_file.close()
    
    return parsed_data

def visualize_days():
    """Visualize data by day of week"""

    #Grab parsed data
    data_file = parse(MY_FILE, ",")

    #Make countervariable to count how many incidents
    #happen per week by iterating through parsed data
    counter = Counter(item["DayOfWeek"] for item in data_file)

    #Seperate x-axis data (day of week) from "counter" 
    #variable from y-axis data (number of incidents)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"],
                ]

    day_tuple = tuple(["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    #Assign y-axis data to matplotlib plot instance
    plt.plot(data_list)

    #Create amount of ticks needed for x-axis, assign labesl
    plt.xticks(range(len(day_tuple)), day_tuple)

    #Save plot
    plt.savefig("Days.png")

    #Close plot file
    plt.clf()

def main():
    visualize_days()

if __name__ == "__main__":
    main()