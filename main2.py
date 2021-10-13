def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    returnList = []
    for item in nums:
        if item % 2 == 0:
            returnList.append(1)
        else:
            returnList.append(0)
    return returnList


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    map = {}
    for item in nums:
        if item in map:
            map[item] += 1
        else:
            map[item] = 1
    
    currentMax = list(map.keys())[0]
    for key in map:
        if map[key] > map[currentMax]:
            currentMax = key
    return currentMax


def main():
    '''The main function is where you will test all of your functions.'''
    # Testing challenge 2
    print("\nTesting oddOrEven")
    print("EXPECTED:", [1, 1, 0, 0, 1, 1], "\nACTUAL:", oddOrEven([2, 4, 5, 7, 8, 10]))
    print("\nTesting mostOccurences")
    print("EXPECTED:", 1, "\nACTUAL:", mostOccurences(oddOrEven([2, 4, 5, 7, 8, 10])))
    print("EXPECTED:", 4, "\nACTUAL:", mostOccurences([2, 4, 5, 7, 4, 10]))
    print("EXPECTED:", 2, "\nACTUAL:", mostOccurences([2, 2, 5, 2, 2, 10]))
    # Add any additional test cases if needed

if __name__ == "__main__":
    main()