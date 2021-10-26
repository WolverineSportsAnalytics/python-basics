def hello_world():
    '''Prints "Hello World!".'''
    print("Hello World")
    return 


def sum(a, b):
    '''Accepts 2 numbers as parameters, returns sum of a and b.'''
    return a + b


def sub(a, b):
    '''Accepts 2 numbers as parameters, returns subtraction of a and b.'''
    return a - b


def product(a, b):
    '''Accepts 2 numbers as parameters, returns product of a and b.'''
    # CHALLENGE: use a for loop and your sum function to implement product
    s = 0
    for i in range(b):
        s = sum(s,a)
    return s


def divide(a, b):
    '''Accepts 2 numbers as parameters, returns a divided by b.'''
    # only pass in numbers that are divisible for sake of implementation
    # CHALLENGE: use a while loop and your sub function to implement divide
    count = 0
    while (a > 0):
            a = sub(a,b)
            count +=1
    return count


def root(num):
    '''Accepts a number as a parameter, returns the sqrt of num.'''
    # only pass in numbers that are perfect squares for sake of implementation
    # leetcode easy
    # CHALLENGE: do not use any built-in Python functions
    if num is 0 or num is 1:
        return num
    a = 1
    result = 1
    while (result < num):
        a+=1
        result = a + a
    return a


def main():
    '''The main function is where you will test all of your functions.'''
    hello_world()
    print("Testing sum:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, sum(2, 3)))
    print("Testing sub:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, sub(7, 2)))
    print("Testing product:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (10, product(2, 5)))
    print("Testing divide:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, divide(10, 2)))
    print("Testing root:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, root(25)))
    # Add any additional test cases if needed

if __name__ == "__main__":
    main()