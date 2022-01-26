def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    list = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            list.append(1)
        else:
            list.append(0)

    return list


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    temp = 1
    mode = 1
    first = nums[0]
    second = first
    i = 1
    for i in range(len(nums)):
        if first == nums[i]:
            temp += 1
            if temp > mode:
                mode = temp
                second = first
        else:
            if temp > mode:
                mode = temp
                second = first
            temp = 1
            first = nums[i]

    return second 


def main():
    '''The main function is where you will test all of your functions.'''
    # Testing challenge 2
    print("\nTesting oddOrEven")
    print("EXPECTED:", [1, 1, 0, 0, 1, 1], "\nACTUAL:", oddOrEven([2, 4, 5, 7, 8, 10]))
    print("\nTesting mostOccurences")
    print("EXPECTED:", 1, "\nACTUAL:", mostOccurences(oddOrEven([2, 4, 5, 7, 8, 10])))
    # Add any additional test cases if needed

if __name__ == "__main__":
    main()