def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        # Reads content from the plaintext file
        with open(filename, "r") as file:
            data = file.read(-1)
            if not data:
                raise ValueError
            array = data.split('\n')
            firstLine = array[0]
            if any(c.isalpha() for c in firstLine):
                raise ValueError
            dimensions = firstLine.split(',')
            if len(dimensions) != 2:
                raise ValueError
            result = []
            if len(array[-1]) == 0:
                del array[-1]
            for line in array:
                if any(c.isalpha() for c in line) or len(line) == 0:
                    print("Error in line: \"{}\"".format(line))
                else: 
                    index = line.split(',')
                    indexX = int(index[0])
                    indexY = int(index[1])
                    result.append((indexX, indexY))

            # result = list(map(lambda x: tuple(map(lambda y: int(y), x.split(','))), array))
            dimensionX = result[0][0]
            dimensionY = result[0][1]
            result.pop(0)
            for i in range(dimensionY):
                for j in range(dimensionX):
                    if ((j,i) not in result):
                        print("H", end ="")
                    else:
                        print(" ", end ="")
                print("")
            # print(index2)
            # print(result)
            # print(str(dimensionX) + " " + str(dimensionY))
            # print(type(array))
            
            # test1.txt
            # Read all the lines in the file and store them to be printed in
            # the proper format. Remember to properly deal with incorrect lines.
            # (hint: arrays are a good choice of data structure)
        
        #
        # Print the image to the console here
        #
    
    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))
    
main()