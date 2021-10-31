#### INCLUDE ANY IMPORTS YOU NEED HERE, DO NOT PIP INSTALL ANY LIBRARIES ####
from random import randint
from math import sqrt, floor
import datetime
from statistics import mean, median, mode
import csv


def perfect_square(num):
    '''Return the sqrt of <num> only if <num> is a perfect square, otherwise return -1.'''
    # Hint: math library
    ans = sqrt(num)

    if floor(ans) * floor(ans) == num:
        return ans

    return -1


def random_num_generator(min, max):
    '''Returns a random number between min and max inclusive.'''
    # Hint: random library
    return randint(min, max)


def get_today():
    '''Returns today's date in the format <month> <day>, <year> where month is a string, day & year are numbers.'''
    # Note: Code must work regardless of today's date
    # Example: November 19, 2021
    # Hint: datetime library
    # Map of month to month
    month = {
        1: "January",
        2: "Feburary",
        # ...
        10: "October",
        11: "November",
        12: "December",
    }
    # Gets date in the format <year>-<month>-<day>
    today = datetime.datetime.now().strftime("%F")
    # Split the formatted date by the separate '-'
    date_obj = today.split('-')

    return month[int(date_obj[1])] + " " + date_obj[2] + ", " + date_obj[0]


def get_stat(nums, type):
    '''Returns <type> of an unsorted list <nums>, where type can be mean, median, mode.'''
    # Example: get_stat([0, 1, 2], "median"), returns 1
    # Hint: statistics library
    if type == "mean":
        return mean(nums)
    elif type == "median":
        return median(nums)
    else: # type is mode
        return mode(nums)


def print_by_profit():
    '''Print data/sales_records.csv in order sorted by profit.'''
    # Hint: csv library
    # Hint: use built-in sort() after parsing csv
    # Hint: figure out how to print out each row in csv first

    with open('data/sales_records.csv') as file:
        # Gets all rows in csv file and put into 2d array
        data_rows = list(csv.reader(file, delimiter=','))

    # Delete first row because it's just the column titles
    print(data_rows.pop(0))

    # Sort by profit (last index of each row)
    data_rows.sort(key=lambda i:float(i[13]))

    # Print each row
    for row in data_rows:
        print(row)
    

def main():
    '''Challenge 3 focuses on using some of Python's built-in functions and libraries.'''
    # Testing challenge 3
    print("\nTesting perfect_square")
    print("EXPECTED:", -1, "\nACTUAL:", perfect_square(24))
    print("EXPECTED:", 5, "\nACTUAL:", perfect_square(25))
    print("\nTesting random_num_generator")
    print("EXPECTED:", "[1, 10]", "\nACTUAL:", random_num_generator(1, 10))
    print("\nTesting get_today")
    print("EXPECTED:", "October 26, 2021", "\nACTUAL:", get_today())
    print("\nTesting get_stat")
    print("EXPECTED:", 1, "\nACTUAL:", get_stat([0, 1, 2], "median"))
    print("\nTesting print_by_profit")
    print_by_profit()
    # Add any additional test cases if needed


if __name__ == "__main__":
    main()