# Medium — Array
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4

from typing import List

# O(n)
class Solution:
    def longestConsecutive(nums: List[int]) -> int:  
        nums = set(nums)
        longest = 0
        
        for num in nums:
            if num-1 not in nums:
                length = 0
                while num + length in nums:
                    length += 1
                longest = max(length, longest)
                
        return longest


