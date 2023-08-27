# Easy — Array
# Given an integer array nums, return true if any value appears **at least twice** in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

from typing import List

# O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        if len(nums) == len(set(nums)):
            return False
                
        return True
