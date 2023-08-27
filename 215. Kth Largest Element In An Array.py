# Medium — Priority Queue
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

from typing import List
import heapq

# O(n + k log n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_arr = [-element for element in nums]

        heapq.heapify(max_arr)

        output = None
        for _ in range(k):
            output = heapq.heappop(max_arr)

        return -output
