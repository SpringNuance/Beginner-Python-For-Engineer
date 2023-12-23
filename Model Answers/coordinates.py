import pandas as pd
import math


def convert(degrees, cardinal_direction):
    minutes = abs(degrees) % 1.0 * 60
    seconds = minutes % 1.0 * 60
    degrees = math.floor(abs(degrees))
    minutes = math.floor(minutes)
    return "{}°{}\'{:.2f}\" {}".format(degrees, minutes, seconds, cardinal_direction)


def lat(degrees):
    if degrees < 0:
        cardinal_direction = "S"
    else:
        cardinal_direction = "N"
    return convert(degrees, cardinal_direction)


def lon(degrees):
    if degrees < 0:
        cardinal_direction = "W"
    else:
        cardinal_direction = "E"
    return convert(degrees, cardinal_direction)


def main():
    read_success = False  # Boolean for defining while-loop (changed to True upon successful read)
    while not read_success:
        filename = input("Enter the name of the file to be read:\n")
        try:
            df = pd.read_csv(filename)
            read_success = True
            print("File read successfully.")
        except OSError:
            print("Error in reading the file '{}'. Please try again.".format(filename))

    cities = df["City"]
    lats = df["Latitude"]
    longs = df["Longitude"]

    print("Conversions are as follows:")
    latitude = list(map(lat, lats))  # Apply function 'lat' to entire list 'lats'
    longitude = list(map(lon, longs))  # Apply function 'lon' to entire list 'longs'

    coordinates = zip(latitude, longitude)  # Combine lats and longs into iterator of tuples

    d = dict(zip(cities, coordinates))  # keys => city name, values => coordinate iterator

    for vals in d:
        print("{}: {}, {}".format(vals, d[vals][0], d[vals][1]))


main()
