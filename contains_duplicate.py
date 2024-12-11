#Given an integer array nums, return true if any value appears more than once 
# in the array, otherwise return false.
def hasDuplicate(nums):
    hashtag = set() #this create a empty set
    for n in nums: #loop through every number
        if n in hashtag: #return true if duplicate found else return false 
            return True
        hashtag.add(n)
    return False

# Take input directly
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the function directly
print("Has duplicates:", hasDuplicate(nums))

