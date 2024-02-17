# Easy - Array, Hash, Divide And Conquer, Sorting
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List

# O(n)
class Solution:
   def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        hashmap = {} 
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        max_count = 0 
        majority_element = None
        for key, value in hashmap.items():
            if value > max_count:
                max_count = value
                majority_element = key
        
        return majority_element