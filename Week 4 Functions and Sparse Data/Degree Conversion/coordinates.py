from decimal import *

def main():
    while (True):
        try: 
            filename = input("Enter the name of the file to be read:\n")
            with open(filename, "r") as file:
                data = file.read(-1)
                #print(data)
            break
        except:
            print(f'Error in reading the file {filename}. Please try again.')
            continue
    
    print("File read successfully.")
    print("Conversions are as follows:")
    data = data.split("\n")
    data.pop(0)
    data = list(map(lambda x: x.split(","), data))
    #print(data)
    city = list(map(lambda x: x[0], data))
    #print(city)
    latitude = list(map(lambda x: float(x[1]), data))
    #print(latitude)
    longitude = list(map(lambda x: float(x[2]), data))
    #print(longitude)
    direction_latitude = list(map(lambda x: 'N' if x > 0 else 'S', latitude))
    #print(direction_latitude)
    direction_longitude = list(map(lambda x: 'E' if x > 0 else 'W', longitude))
    #print(direction_longitude)
    absolute_latitude =  [abs(i) for i in latitude]
    #print(absolute_latitude)
    absolute_longitude =  [abs(i) for i in longitude]
    #print(absolute_longitude)
    ####
    degree_latitude = [int(i) for i in absolute_latitude]
    #print(degree_latitude)
    degree_longitude = [int(i) for i in absolute_longitude]
    #print(degree_longitude)
    ####
    minute_latitude = [int(60 * (absolute_latitude[i] - degree_latitude[i])) for i in range(len(absolute_latitude))]
    #print(minute_latitude)
    minute_longitude = [int(60 * (absolute_longitude[i] - degree_longitude[i])) for i in range(len(absolute_longitude))]
    #print(minute_longitude)
    ###
    second_latitude = [3600 * absolute_latitude[i] - 3600 * degree_latitude[i] - 60 * minute_latitude[i] for i in range(len(absolute_latitude))]
    #print(second_latitude)
    second_longitude = [3600 * absolute_longitude[i] - 3600 * degree_longitude[i] - 60 * minute_longitude[i] for i in range(len(absolute_longitude))]
    #print(second_longitude)
    latitude = list(zip(degree_latitude, minute_latitude, second_latitude, direction_latitude))
    #print(latitude)
    longitude = list(zip(degree_longitude, minute_longitude, second_longitude, direction_longitude))
    #print(longitude)
    allInfo = list(zip(city, latitude, longitude))
    #print(allInfo)
    # "{}°{}\'{:.2f}\" {}".format(degrees, minutes, seconds, cardinal_direction)
    for info in allInfo:
        cityName = info[0]
        latitudeFormat = "{}°{}\'{:.2f}\" {}".format(info[1][0], info[1][1], info[1][2], info[1][3])
        longitudeFormat = "{}°{}\'{:.2f}\" {}".format(info[2][0], info[2][1], info[2][2], info[2][3])
        print(f'{cityName}: {latitudeFormat}, {longitudeFormat}')

main()
# test1.csv
'''
x = [1, 2, 3]
y = [4, 5, 6]
z = ["a", "b", "c"]
print(list(zip(x, y, z)))
print(zip([x, y, z]))
print(list(zip(zip(x, y), z)))
print([(a, b, c) for a in x for b in y for c in z])
print([(x[i], y[i], z[i]) for i in range(0, 3)])
'''
