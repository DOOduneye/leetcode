# Medium — Two Pointer
# Given a 1-indexed array of integers numbers that is already *sorted in non-decreasing order*, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return *the indices of the two numbers,* index1 *and* index2*, added by one as an integer array* [index1, index2] *of length 2.*
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. 

from typing import List

class Solution:
    # O(n^2)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if target - numbers[i] == numbers[j] and j != i:
                    i+=1
                    j+=1
                    return [i, j]


    # O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        i, j = 0, len(numbers) - 1 
        while i < j:
            total = numbers[j] + numbers[i]
            if total == target:
                i+= 1
                j+= 1
                return [i, j]
            if total > target:
                j -= 1
            else:
                i += 1

