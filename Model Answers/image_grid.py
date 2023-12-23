# BPfE SPRING 2022
# Beginner's Python For Engineers
# Author: Aaron Campbell & Visa Mäkeläinen
# Example solution for Exercise 1.1 Image Grid

BASE_CHARACTER = "H"
SELECTION_CHARACTER = " "

def main():
    filename = input("Enter the name of the file to be read:\n")
    try:

        # Reads content from the plaintext file
        with open(filename, "r") as file:
            dimensions = file.readline().rstrip().split(',')  # Reads array dimensions from file
            lines = file.read().splitlines()  # Saves remaining lines into list
        arrayWidth = int(dimensions[0])
        arrayHeight = int(dimensions[1])

        # Generates grid (nested list) of 'H' characters based on the given dimensions
        grid = []
        for y in range(arrayHeight):
            row = []
            for x in range(arrayWidth):
                row.append(BASE_CHARACTER)
            grid.append(row)

        # Punches holes into grid, by replacing 'H' characters with empty spaces
        for line in lines:
            try:
                if line == "":
                    raise ValueError
                coords = line.split(',')
                grid[int(coords[1])][int(coords[0])] = SELECTION_CHARACTER
            except (ValueError, IndexError):
                print("Error in line: \"{}\"".format(line))

        # Prints grid
        for row in grid:
            row_string = "".join(row)
            print(row_string)

    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))


main()
