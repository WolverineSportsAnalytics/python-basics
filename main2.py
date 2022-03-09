def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    size = len(nums)
    for x in range(size):
        if nums[x] % 2 == 0:
            nums[x] = 1
        else:
            nums[x] = 0
    return nums


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    current_total = 0
    max_count = 1
    most = nums[0]
    for x in range(1,nums):
        if nums[x-1] == nums[x]:
            current_total += 1
        else:
            if current_total > max_count:
                most = nums[x-1]
                max_count = current_total
        current_total = 1
    if current_total > max_count:
        max_count = current_total
        most = nums[-1] # -1 is used to obtain the element at the last index as it is the most frequent element
        return most
                
    
    return most # last element is not the most frequent element


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
