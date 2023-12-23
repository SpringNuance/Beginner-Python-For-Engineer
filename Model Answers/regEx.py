import pandas as pd

"""
Complete the missing regular expression (regex = ) arguments between the quotation marks ""
so as to filter the dataset to provide the described subset. You may edit the main program to
create your own tests. Do not modify the test functions beyond the regex variable definition.
"""


def test1(df):
    # fill in here for usernames starting with vowels

    regex = "^[aeiouAEIOU]"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def test2(df):
    # fill in here for usernames having 2 consecutive vowels

    regex = ".*[aeiouAEIOU]{2}.*"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def test3(df):
    # fill in here for usernames not containing any special characters

    regex = "^[a-zA-Z0-9]+$"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def test4(df):
    # fill in here for usernames ending with a number

    regex = ".*\d$"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def test5(df):
    # Filter the dataset to match the following pattern:

    #       AG_Tambo19
    #       AG_Rex17
    #       AG_Peeta13
    #       AG_Orneal22
    #       AG_Karl05

    # # Example invalid entries such as:
    #   AH_Tambo19
    #   AG-Rex17
    #   AG_peeta13
    #   AG_Orneal2
    #   AG_Karl5
    # #

    regex = "^AG_[A-Z].*[0-9][0-9]$"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def main():
    filename = input("Enter the name of the file to be read:\n")

    try:
        df = pd.read_csv(filename)
        print("\nOutput from function 1: \n" + test1(df))
        print("\nOutput from function 2: \n" + test2(df))
        print("\nOutput from function 3: \n" + test3(df))
        print("\nOutput from function 4: \n" + test4(df))
        print("\nOutput from function 5: \n" + test5(df))

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))

if __name__ == "__main__":
    main()
