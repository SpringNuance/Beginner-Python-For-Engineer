import numpy as np
import pandas as pd
import datetime

DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]

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
    fileNames = []
    fileData = {}
    for i in range(1,4):
        while True:
            try: 
                filename = input(f"Enter the name of file #{i}:\n")
                if filename in fileNames:
                    print(f"File {filename} is already included in this analysis. Please choose a different file.")
                else:
                    with open(filename, "r"):
                        fileNames.append(filename)
                        df = pd.read_csv(filename, sep="\t", dtype=str)
                        fileData[filename] = df
                    break
            except FileNotFoundError:
                print(f'Error in reading file {filename}. Closing program.')
                return

    for filename in fileData:
    # format date-time
        date_format = get_date_format(fileData[filename]['date']) # Gets an appropriate date format for the DataFrame
        fileData[filename]['date'] = pd.to_datetime(fileData[filename]["date"], format=date_format) # Converts column values to DateTime objects
        fileData[filename]['date'] = fileData[filename]['date'].dt.date  # Removes time value from DateTime object
    # format cases
        fileData[filename]['cases'] = fileData[filename]['cases'].str.replace(" ", "",regex=True)
        fileData[filename]['cases'] = fileData[filename]['cases'].str.replace(",", "",regex=True)
        fileData[filename]['cases'] = fileData[filename]['cases'].str.replace(".", "",regex=True)
        fileData[filename]['cases'] = pd.to_numeric(fileData[filename]['cases'], errors='coerce')

    dataframe1 = fileData[fileNames[0]]
    dataframe2 = fileData[fileNames[1]]
    dataframe3 = fileData[fileNames[2]]
    dataNames = list(map(lambda x: x[:-4], fileNames))
    column_names = ['date', f'cases_{dataNames[0]}', f'cases_{dataNames[1]}', f'cases_{dataNames[2]}']

    merged_dataframe = pd.merge(dataframe1, dataframe2, how='outer', on='date')
    merged_dataframe = pd.merge(merged_dataframe, dataframe3, how='outer', on='date')
    merged_dataframe.columns = column_names
    print("\nPrinting summary statistics:")
    print(merged_dataframe.describe())
    print("\nPrinting first five rows:")
    print(merged_dataframe.head())

    # .tsv
        
    '''
    check = True
    while check:
        filenameSplit = filename.split('.')
        extension = filenameSplit[1]
        if extension == "csv": 
            try:
                df = pd.read_csv(filename)
                check = False
            except:
                print(f"Error in reading the file '{filename}'. Please try again.")
                filename = input("Enter the name of the file to be read:\n")
        elif extension == "xls":
            try:
                df = pd.read_excel(filename)
                check = False
            except:
                print(f"Error in reading the file '{filename}'. Please try again.")
                filename = input("Enter the name of the file to be read:\n")
        elif extension == "json":
            try:
                df = pd.read_json(filename)
                check = False
            except:
                print(f"Error in reading the file '{filename}'. Please try again.")
                filename = input("Enter the name of the file to be read:\n")
        else:
            print(f"File extension '.{extension}' is not supported. Please try again.")
            filename = input("Enter the name of the file to be read:\n")
    
    print("File read successfully.\n")
    print("Printing summary statistics:\n")
    print(df.describe())
    # three_numbers.csv
    '''

main()