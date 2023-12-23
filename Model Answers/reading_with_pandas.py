# BPfE SPRING 2022
# Beginner's Python For Engineers
# Author: Visa Mäkeläinen
# Example solution for Exercise 1.2 Reading with Pandas

import pandas as pd

FILETYPE_FUNCTIONS = {'csv': pd.read_csv, 'xls': pd.read_excel, 'json': pd.read_json}


def read_file(filename):
    # Attempts to read dataset files into DataFrames using the filename parameter
    # If successful, returns the DataFrame and True
    # If not, prints error message and returns None and False
    file_extension = filename.split(".")[-1]
    if file_extension in FILETYPE_FUNCTIONS:
        try:
            df = FILETYPE_FUNCTIONS[file_extension](filename)
            print("File read successfully.")
            return df, True
        except OSError:
            print("Error in reading the file '{}'. Please try again.".format(filename))
            return None, False
    else:
        print("File extension '.{}' is not supported. Please try again.".format(file_extension))
        return None, False


def main():
    read_success = False  # Boolean for defining while-loop
    while not read_success:
        filename = input("Enter the name of the file to be read:\n")
        df, read_success = read_file(filename)
    print("\nPrinting summary statistics:")
    print(df.describe())  # Prints summary statistics for the dataset


main()
