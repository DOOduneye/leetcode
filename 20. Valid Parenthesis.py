# Problem 20
# Easy — Stack
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Input: s = "(){}"
# Output: true

# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or bracket_map[char] != stack.pop():
                    return False

        return len(stack) == 0
            

