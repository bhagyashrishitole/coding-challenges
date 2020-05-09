"""
Problem Statement
Majority Element
Solution
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = int(len(nums) / 2)

        """ Solution-1"""
        # nums_set = set(nums)
        # for each in nums_set:
        #     if nums.count(each) > majority:
        #         return each

        """Solution-2"""
        count = {}
        for each in nums:
            count[each] = count.get(each, 0) + 1
            if count[each] > majority:
                return each

        """Solution-3"""
        # nums.sort()
        # return nums[majority]
        """Solution-4"""
        # return collections.Counter(nums).most_common()[0][0]

        """Solution-4"""
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                res = nums[i]
            if res == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return res
