from typing import List

def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    # For example 4#hello5#world
    return res

def decode(s: str) -> List[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res

# Example input
strings = ["hello", "world"]
encoded = encode(strings)
print("Encoded:", encoded)

decoded = decode(encoded)
print("Decoded:", decoded)
