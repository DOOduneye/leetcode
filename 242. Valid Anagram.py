# Problem 242 
# Easy — Array
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true

# O(n)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_1, hashmap_2 = {}, {}

        for i in range(len(s)):
            if s[i] in hashmap_1:
                hashmap_1[s[i]] += 1
            else:
                hashmap_1[s[i]] = 1
            
            if t[i] in hashmap_2:
                hashmap_2[t[i]] += 1
            else:
                hashmap_2[t[i]] = 1

        return hashmap_1 == hashmap_2
