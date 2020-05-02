# Jewels and Stones

"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

# Approach1: Linear search
# 1. For every stone in S, check if that is a jewel in J 

# Time Complexity - O(nxm) where n is the length of J and m is length of S
# Space Complexity - O(1)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count
		
# Approach2: Using HashSet
# 1. Store the jewels in a HashSet
# 2. Check for every stone, if that is in the HashSet
# 3. If it is not present, do nothing. If it is present, increse count by 1.

# Time Complexity - O(n + m) where n is the length of J for creating the hashset and m is length of S while traversing
# Space Complexity - O(n) extra space for hashset of length equal to lenght of J

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashSet = set()
        count = 0
        for j in J:
            hashSet.add(j)
        for s in S:
            if s not in hashSet:
                continue
            else:
                count += 1
        return count
