# Ransom Note

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""

"""
Approach: Using Hash table
1. Traverse the ransomNote string and store each letter's count in a hash table
2. Travrse the magazine string and for each letter in magazine, check if that letter is there in ransom hash table. If it is present, reduce its count by 1.
3. Finally, check if all the values in the hash table is 0, then it means we have got letters from magazine for all the letters in ransomNote. Otherwise, return False.
"""

# Time Complexity - O(n+m+n) Hash map creation,magazine traversal and hash values traversal 
# Space Complexity - O(n) for using hash map

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_table = dict()
        for r in ransomNote:# O(n)
            if r not in ransom_table:
                ransom_table[r] = 1
            else:
                ransom_table[r] += 1
        for m in magazine:#O(m)
            if m in ransom_table:
                ransom_table[m] -= 1
        for val in ransom_table.values():#O(n)
            if val > 0:
                return False
        return True