def oddOrEven(nums):
    '''Given an unsorted list of numbers, return a list that indicates if the value at each index is odd (0) or even (1).'''
    # EXAMPLE:
    # Given [2, 4, 5, 7, 8, 10], return [1, 1, 0, 0, 1, 1]
    ans=[0]*len(nums)
    for i in range(len(nums)):
        if (nums[i] % 2 == 0):
            ans[i] = 1
            
    return ans


def mostOccurences(nums):
    '''Given an unsorted list of numbers, returns the value that occured the most in nums.'''
    # Hint: use oddOrEven to test function faster
    # Hint: use a map
    # Hint: https://stackoverflow.com/questions/13098638/how-to-iterate-over-the-elements-of-a-map-in-python
    occurs={}
    max_occ= 0
    max_val=0
    for i in nums:
        if i in occurs.keys():
            occurs[i] = occurs[i] + 1
        else:
            occurs[i] = 1
            
        if occurs[i] > max_occ:
            max_occ = occurs[i]
            max_val = i
    
    return max_val 


def main():
    '''The main function is where you will test all of your functions.'''
    # Testing challenge 2
    print("\nTesting oddOrEven")
    print("EXPECTED:", [1, 1, 0, 0, 1, 1], "\nACTUAL:", oddOrEven([2, 4, 5, 7, 8, 10]))
    print("\nTesting mostOccurences")
    print("EXPECTED:", 1, "\nACTUAL:", mostOccurences(oddOrEven([2, 4, 5, 7, 8, 10])))
    print("EXPECTED:", 7, "\nACTUAL:", mostOccurences([2, 7, 7, 7, 8, 7]))

if __name__ == "__main__":
    main()