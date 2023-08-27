# Medium — Sliding Window
# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        repeating_set = set()

        l, r = 0, 0

        while r < len(s):
            while s[r] in repeating_set:
                repeating_set.remove(s[l])
                l += 1
            repeating_set.add(s[r])
            r += 1
            max_length = max(max_length, r - l)

        return max_length

