# BPfE SPRING 2022
# Beginner's Python For Engineers
# Author: Visa Mäkeläinen
# Example solution for Exercise 2.1 Covid Statistics

import pandas as pd
import numpy as np
import datetime

DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]
THOUSANDS_SEPARATORS = [',', '.', ' ']


def get_date_format(dates):
    # Gets a Pandas Series of dates as strings and attempts to convert each string to a DateTime object
    # Conversion is attempted with every format in 'DATE_FORMATS' list
    # Returns a date format that works for all date strings
    for date_format in DATE_FORMATS:
        reject_format = False
        i = 0
        while not reject_format:
            try:
                datetime.datetime.strptime(dates[i], date_format)
                if (i + 1) == len(dates):
                    return date_format
            except ValueError:
                reject_format = True
            i += 1
    raise Exception('An error occurred: no valid date format found.')


def main():
    dataframes = []
    filenames = []
    column_names = ['date']

    try:
        # Attempts to read three files
        for i in range(3):
            user_input = (input("Enter the name of file #{}:\n".format(i + 1))).lower()
            while user_input in filenames:
                print(
                    "File {} is already included in this analysis. Please choose a different file.".format(user_input))
                user_input = (input("Enter the name of file #{}:\n".format(i + 1))).lower()
            filenames.append(user_input)
            dataframes.append(pd.read_csv(filenames[i], sep="\t", dtype=str))
            column_names.append("cases_" + filenames[i][:-4])

        # Converts 'cases' column to numbers and 'date' column to DateTime.Date objects
        for df in dataframes:
            for char in THOUSANDS_SEPARATORS:
                df['cases'] = df['cases'].str.replace(char, '')
            df['cases'] = pd.to_numeric(df['cases'], errors='coerce')
            date_format = get_date_format(df['date'])
            df['date'] = pd.to_datetime(df['date'], format=date_format)
            df['date'] = df['date'].dt.date  # Removes time value from DateTime object

        # Merges three DataFrames and changes column names to match 'column_names' list
        df = pd.merge(dataframes[0], dataframes[1], how='outer', on='date')
        df = pd.merge(df, dataframes[2], how='outer', on='date')
        df.columns = column_names
        print()

        # Prints summary statistics of merged DataFrame
        print("Printing summary statistics:")
        print(df.describe())
        print()

        # Prints first five rows of merged DataFrame
        print("Printing first five rows:")
        print(df.head())
        print()

    except OSError:
        # If file cannot be read, prints notice
        print("Error in reading file {}. Closing program.".format(filenames[-1]))


main()
