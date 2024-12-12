from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    # Create a dictionary
    freq = [[] for i in range(len(nums) + 1)]
    # This line will create freq=[[],[],[],[]] type of output

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    # Count how many times each number is repeated
    for num, cnt in count.items():
        freq[cnt].append(num)
    # Put the values as per their index in freq list 

    res = []
    for i in range(len(freq) - 1, 0, -1):
        # Decrement values from highest to lowest
        for num in freq[i]:
            res.append(num)
            # Add the values to res 
            if len(res) == k:
                return res

# Example input
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
