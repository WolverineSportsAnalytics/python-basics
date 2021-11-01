#### INCLUDE ANY IMPORTS YOU NEED HERE, DO NOT PIP INSTALL ANY LIBRARIES ####
import random
from datetime import datetime
import statistics
import pandas as pd


def perfect_square(num):
    '''Return the sqrt of <num> only if <num> is a perfect square, otherwise return -1.'''
    # Hint: math library
    sqrt = int(num**0.5)
    if sqrt ** 2 == num:
        return sqrt
    else:
        return -1


def random_num_generator(min, max):
    '''Returns a random number between min and max inclusive.'''
    # Hint: random library
    return random.uniform(min, max)


def get_today():
    '''Returns today's date in the format <month> <day>, <year> where month is a string, day & year are numbers.'''
    # Note: Code must work regardless of today's date
    # Example: November 19, 2021
    # Hint: datetime library
    today = datetime.now()
    return today.strftime("%B %d, %Y")


def get_stat(nums, type):
    '''Returns <type> of an unsorted list <nums>, where type can be mean, median, mode.'''
    # Example: get_stat([0, 1, 2], "median"), returns 1
    # Hint: statistics library
    if type == "median":
        return statistics.median(nums)
    elif type == "mean":
        return statistics.mean(nums)
    elif type == "mode":
        return statistics.mode(nums)


def print_by_profit():
    '''Print data/sales_records.csv in order sorted by profit.'''
    # Hint: csv library
    # Hint: use built-in sort() after parsing csv
    # Hint: figure out how to print out each row in csv first
    print("Working with csvs!")
    df = pd.read_csv("sales_records.csv")
    df.sort_values("Total Profit", inplace=True, ascending=False)
    df.reset_index(inplace=True)
    print(df)

    return None


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