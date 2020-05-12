"""
Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        """Solution-1"""
        while (start < end):
            mid = (start + end) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 2
                else:
                    end = mid - 2
        return nums[start]

        """Solution-2 Improved from above by combining conditions"""
        while(start < end):
            mid = (start + end)//2
            comp = mid + 1 if mid%2 == 0 else mid - 1
            if nums[mid] == nums[comp]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

        """Solution from discussion forum"""
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
