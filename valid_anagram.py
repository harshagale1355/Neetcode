#Given two strings s and t, return true if the 
# two strings are anagrams of each other,
#  otherwise return false
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {} #create two dictionarys, they will contain string and how many they are repeated
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT #if there count is equal, it will return true otherwise false


# Take input from the user
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Call the function and print the result
print("Are the strings anagrams?", isAnagram(s, t))
