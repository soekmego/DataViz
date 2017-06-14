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

def visualize_type():
    """Visualize data by category in bar graph"""

    #Grab parsed data
    data_file = parse(MY_FILE, ",")

    #Make new countervariable and count incidents by category
    counter = Counter(item["Category"] for item in data_file)

    #Set labels based on key of counter
    labels = tuple(counter.keys())

    #Set where label hits x-axis
    xlocations = np.arrange(len(labels)) + 5

    #Width of each bar that will be plotted
    #Assign data to a bar plot
    #Assign label and tick location to x-axis
    plt.xticks(xlocations + Width / 2, labels, rotation=90)

    #Give room enough so x-axis wont be cut off on graph
    plt.subplot_adjust(bottom=0.4)

    #Make overall graph large enough
    plt.rcParams["figure.figsize"] = 12, 8

    #Save graph
    plt.savefig()

    #Close plot figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()