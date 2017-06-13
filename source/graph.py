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

#TODO - def visualize_days()