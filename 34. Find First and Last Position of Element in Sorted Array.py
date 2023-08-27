# Medium — Binary Search, Two Pointer
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

from typing import List

# O (log n)
class Solution: 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            if nums[l] < target:
                l += 1
            if nums[r] > target:
                r -= 1

        return [-1, -1]