"""
Problem Statement
First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Solution-1"""
        #         from collections import OrderedDict
        #         char_count = {}

        #         for i, each in enumerate(s):
        #             if char_count.get(each):
        #                 char_count[each] = [char_count[each][0], char_count[each][1]+1]
        #             else:
        #                 char_count[each] = [i, 1]
        #         for each in char_count:
        #             if char_count[each][1] == 1:
        #                 return char_count[each][0]
        #         return -1
        """ Solution-2 """
        # c = collections.Counter(s)
        # for i in range(len(s)):
        #     if c[s[i]]==1:
        #         return i
        # return -1

        """Solution-3"""
        return min((s.index(l) for l in 'abcdefghijklmnopqrstuvwxyz' if s.count(l) == 1), default=-1)
