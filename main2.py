def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    return [int(i % 2 == 0) for i in nums]


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    return max(nums, key=nums.count)


def main():
    '''The main function is where you will test all of your functions.'''
    # Testing challenge 2
    print("\nTesting oddOrEven")
    print("EXPECTED:", [1, 1, 0, 0, 1, 1], "\nACTUAL:", oddOrEven([2, 4, 5, 7, 8, 10]))
    print("\nTesting mostOccurences")
    print("EXPECTED:", 1, "\nACTUAL:", mostOccurences(oddOrEven([2, 4, 5, 7, 8, 10])))
    # Add any additional test cases if needed
    print("\noddOrEven Test 2\n")
    print("EXPECTED:", [1, 0, 0, 1, 1, 0], "\n")
    print("ACTUAL:", oddOrEven([8, 7, 11, 100, -2, 3]), "\n")
    print("mostOcurrences Test 2\n")
    print("EXPECTED: 4\n")
    print("ACTUAL:", mostOccurences([1, 4, 2, 2, 4, 3, 3, 3, 4, 4]))

if __name__ == "__main__":
    main()