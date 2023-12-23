import datetime


def main():
    dt_now = datetime.datetime.now()
    xmas_check = lambda x: True if x.month == 12 else False
    xmas_countdown = lambda x: 12 - x.month
    bedtime_check = lambda x: True if x.hour >= 21 else False
    bedtime_countdown = lambda x: (20 - x.hour, 59 - x.minute, 60 - x.second)

    print("Welcome to Christmas countdown!")
    print("Is Christmas this month?")
    if xmas_check(dt_now):
        print("Yes! ", end="")
    else:
        print("Nope, but the number of months until December is: {:d}".format(xmas_countdown(dt_now)))
    print("Let's make Santa happy and go to sleep early!")
    if bedtime_check(dt_now):
        print("It's already past your bedtime! Time to go to bed!")
    else:
        print("You have {:d} hours, {:d} minutes, and {:d} seconds until bedtime.".format(*bedtime_countdown(dt_now)))


main()
