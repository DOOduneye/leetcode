# Medium — Array
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import List
from collections import defaultdict

class Solution:
    # O(n * m * log(m))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [['']]

        sorted_strs = []
        for value in strs:
            sorted_strs.append(''.join(sorted(value)))
        
        hashmap = {}
        for i, value in enumerate(sorted_strs):
            if value in hashmap:
                hashmap[value].append(i)
            else:
                hashmap[value] = [i]
        
        output = []
        for key, value in hashmap.items():
            inner = []
            for i in value:
                inner.append(strs[i])
        
            output.append(inner)
        
        return output
    
    # O (n * m) 
    def groupAnagramsOptimal(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
            
        for value in strs:
            count = [0] * 26
            for c in value:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(value)
            
        return list(hashmap.values())

    # O(n * m * log(m))
    def groupAnagramsPythonic(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
            
        for value in strs:
            sorted_value = ''.join(sorted(value))
            hashmap[sorted_value].append(value)
            
        return list(hashmap.values())
