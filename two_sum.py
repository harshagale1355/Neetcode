#Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numbers = {} #will contain number and there index
    for i, n in enumerate(nums):
        diff = target - n # Ex. [1,2,3,4] target=3 , 3 - 1 = 2, if 2 found, return n and diff indices
        if diff in numbers:
            return [numbers[diff], i]
        numbers[n] = i

# Take input from the user
nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

# Call the function and print the result
result = twoSum(nums, target)
print("Indices of the two numbers:", result)
