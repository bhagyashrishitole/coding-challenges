"""
Problem Statement

Valid Perfect Square
Solution
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""
from math import log
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        start = int(log(num, 2))
        end = num//2 + 1
        mid = (start + end)// 2
        while (start <= end):
            if mid**2 == num:
                return True
            elif mid**2 < num:
                start=mid + 1
            else:
                end = mid - 1
            mid = (start + end)// 2
        return False