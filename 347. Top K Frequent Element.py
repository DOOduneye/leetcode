# Medium — Array
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from collections import Counter
from collections import defaultdict
from typing import List
import heapq

class Solution:
    # O(n log k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1

        frequency = [(-freq, num) for num, freq in hashmap.items()]
        heapq.heapify(frequency)

        output = []
        for _ in range(k):
            output.append(heapq.heappop(frequency)[1])

        return output


    # O(n)
    def topKFrequentOptimal(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count [n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

