# Medium — Array
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

from typing import List

class Solution:
    # O(n) | O(n) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])
        
        counter = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            postfix.append(postfix[(len(nums) - 1) - counter] * nums[i-1])
            counter-=1
        
        postfix = postfix[::-1]
        
        output = []
        for i in range(0, len(nums)):
            if i == 0:
                print(nums[i], postfix[i+1])
                output.append(1 * postfix[i+1])
            elif i == len(nums) - 1:
                output.append(1 * prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])

        return output


    # O(n) | O(1) space
    def productExceptSelfOptimal(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res