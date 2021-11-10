def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]

    solution = []

    # Push into solution as we determine if num is even or odd
    for num in nums:
        if num % 2 == 0:
            solution.append(1)
        else:
            solution.append(0)

    # Likewise, can also just replace the indexes of nums
    # for i, num in enumerate(nums):
    #     if num % 2 == 0:
    #         nums[i] = 1
    #     else:
    #         nums[i] = 0

    return solution     # return nums if use second solution


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python

    uniqueCount = {}

    for num in nums:
        # Check if key already exists, if so, just add one to count
        if num in uniqueCount:
            uniqueCount[num] += 1
        # Key doesn't exist, set count to 1
        else:
            uniqueCount[num] = 1

    answer = -1     # answer to keep track of the key
    maxCount = 0    # maxCount to keep track of max count we've seen in uniqueCount
    for key in uniqueCount:
        if uniqueCount[key] > maxCount:
            answer = key                    # update answer
            maxCount = uniqueCount[key]     # update maxCount

    return answer


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