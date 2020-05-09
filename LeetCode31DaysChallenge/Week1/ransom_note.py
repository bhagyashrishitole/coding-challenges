"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return not len(Counter(ransomNote) - Counter(magazine)) --> one liner with counter

        magazine_dict = {}
        for each in magazine:
            magazine_dict[each] = magazine_dict.get(each, 0) + 1

        for each in ransomNote:
            if not magazine_dict.get(each, 0):
                return False
            magazine_dict[each] -= 1

        return True
