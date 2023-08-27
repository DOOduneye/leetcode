# Easy — Array
# Given an integer array nums, return true if any value appears **at least twice** in the array, and return false if every element is distinct.

from typing import List

# O(n)
def containsDuplicate(self, nums: List[int]) -> bool:        
  if len(nums) == len(set(nums)):
    return False
        
  return True
