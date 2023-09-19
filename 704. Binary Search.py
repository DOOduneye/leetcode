# Easy — Array
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

from typing import List
from functools import lru_cache

# O(log n)
class Solution:
    # Recursive
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums))
        
    @lru_cache
    def binarySearch(self, nums: List[int], target: int, low: int, high: int) -> int:
        middle = (low + high) // 2
        
        if target < middle:
            self.binarySearch(nums, target, low, middle)
        elif target > middle:
            self.binarySearch(nums, target, middle + 1, high)
        else:
            return nums[middle]

    # Iterative 
    def binarySearchIterative(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right: 
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1