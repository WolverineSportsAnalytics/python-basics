def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    list1 = []
    for x in nums:
            if x%2 == 0:
                list1 += [1]
            else: 
                list1 += [0]
    return list1


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

    answer = 0     # answer to keep track of the key
    maxCount = 0    # maxCount to keep track of max count we've seen in uniqueCount
    for k in uniqueCount:
        if uniqueCount[k] > maxCount:
            answer = k                    # update answer
            maxCount = uniqueCount[k]     # update maxCount

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