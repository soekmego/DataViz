"""
Data Visualization Project

Parse data from an CSV or Excel File, render in GeoJSON
save to a database and visualize in graph form

This project is for educational purposes.
"""

import geojson
import parse as p

def create_map(data_file):
    """Create a GeoJSON file.

    Retuns a GeoJSON file that can be rendered in a GitHub
    Gist at gists.github.com. Copy the output file and
    paste into a new Gist, then create either a public or
    private gist. GitHub will automatically render the GeoJSON
    file as a map.
    """

    #Define GeoJSON type
    geo_map = {"type": "FeatureCollection"}

    #Define empty list to collect each point to graph
    item_list = []

    #Iterate over our data to create GeoJSON document.
    #Use neumerate() to get the line, aswell
    #the index.
    for index, line in enumerate(data_file):

        #Skip 0 coordinates as this would cause bugs
        if line["X"] == "0" or line["Y"] == "0":
            continue

        #Set up new dictionary for each iteration
        data = {}

        #Assign line items to appropiate GeoJSON fields.
        data["type"] = "Feature"
        data["id"] = index
        data["properties"] = {"title": line["Category"],
                            "description": line["Descript"],
                            "date": line["Date"]}
        data["geometry"] = {"type": "Point",
                            "coordinates": (line["X"], line["Y"])}

        #Add data dictionary to item_list
        item_list.append(data)

    #For each item in the item_list we add a point to a dictionary
    #setdefault creates a key called "features" that has a value
    #type of an empty list. With each iteration, a point appends
    #to that list.
    for point in item_list:
        geo_map.setdefault("features", []).append(point)

    #All data is parsed in GeoJSON, now write file to upload
    with open("file_sf.geojson", "w") as f:
        f.write(geojson.dumps(geo_map))


def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()