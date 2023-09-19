# Medium — Sliding Window
# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.\

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

from typing import List

# O(n)
class Solution:
    def longest_substring_with_k_distinct_characters(arr: List[int], k: int) -> int:
        hashmap = {}
        max_length = 0

        l, r = 0, 0
        while r < len(arr):
            if arr[r] not in hashmap:
                hashmap[arr[r]] = 1
            else:
                hashmap[arr[r]] += 1

            while len(hashmap) > k:
                hashmap[arr[l]] -= 1
                if hashmap[arr[l]] == 0:
                    hashmap.pop(arr[l])

                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length