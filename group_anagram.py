#Given an array of strings strs, group all anagrams together into sublists.
#You may return the output in any order.
from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = collections.defaultdict(list) # Automatically initializes each new key with an empty list ([])
    for s in strs:
        count = [0] * 26  #create list [0,0,0,....0] for 26 letter
        for letter in s:
            count[ord(letter) - ord('a')] += 1 # If the letter is found it increment its occurrence
        d[tuple(count)].append(s) 
    return list(d.values())

# Take input from the user
strs = input("Enter a list of words separated by spaces: ").split()

# Call the function and print the result
result = groupAnagrams(strs)
print("Grouped Anagrams:", result)
