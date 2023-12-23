from datetime import datetime

def main():
    print("Welcome to Christmas countdown!")
    print("Is Christmas this month?")
    time = datetime.now()    
    isDecember = lambda month: month != 12
    tillDecember = lambda month: 12 - month if month < 12 else month - 12
    if isDecember(time.month): 
        print("Nope, but the number of months until December is: {:d}".format(tillDecember(time.month)))
        print("Let's make Santa happy and go to sleep early!")
    else:
        print("Yes! Let's make Santa happy and go to sleep early!")
   
    past21h = lambda time: not(time.hour < 21 or (time.hour == 21 and time.minute == 0 and time.second == 0))
    till21h = lambda time: (21 - time.hour - 1, 60 - time.minute - 1, 60 - time.second)
    if not past21h(time):
        print("You have {:d} hours, {:d} minutes, and {:d} seconds until bedtime.".format(*till21h(time)))
    else:
        print("It's already past your bedtime! Time to go to bed!")

main()