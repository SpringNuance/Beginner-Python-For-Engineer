
import pandas as pd

def main():
    filename = input("Enter the name of the file to be read:\n")

    check = True
    while check:
        #if not os.path.isfile(filename):
        #    print(f"Error in reading the file '{filename}'. Please try again.")
        #    filename = input("Enter the name of the file to be read:\n")
        #else: 
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

main()