def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    output = []
    for x in nums:
        if (x % 2 == 0):
            output.append(1)
        else:
            output.append(0)
    return output


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    occurences = {}
    for x in nums:
        if (x in occurences):
            occurences[x] += 1
        else:
            occurences[x] = 1
    
    number = -1
    maximum = 0
    for index in occurences:
        if (occurences[index] > maximum):
            number = index
            maximum = occurences[index]
    
    return number

def main():
    '''The main function is where you will test all of your functions.'''
    # Testing challenge 2
    print("\nTesting oddOrEven")
    print("EXPECTED:", [1, 1, 0, 0, 1, 1], '\nACTUAL:', oddOrEven([2, 4, 5, 7, 8, 10]))
    print("\nTesting mostOccurences")
    print("EXPECTED:", 1, "\nACTUAL:", mostOccurences(oddOrEven([2, 4, 5, 7, 8, 10])))
    # Add any additional test cases if needed

if __name__ == "__main__":
    main()