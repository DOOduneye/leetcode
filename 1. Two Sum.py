# Easy — Array
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import List

class Solution:
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        hashmap = {}

        for i in range(0, len(nums)):
            hashmap[nums[i]] = i

        for i in range(0, len(nums)):
            find = target - nums[i]
            if find in hashmap and hashmap[find] != i:
                return [hashmap[find], i]
    
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        hashmap = {}

        for i in range(0, len(nums)):
            find = target - nums[i]
            if find in hashmap:
                return [hashmap[find], i]
            hashmap[nums[i]] = i
