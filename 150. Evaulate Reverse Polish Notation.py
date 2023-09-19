# Medium — Stack
# You are given an array of strings tokens that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).
# Evaluate the expression. Return *an integer that represents the value of the expression*.
# Note that:
# - The valid operators are '+', '-', '*', and '/'.
# - Each operand may be an integer or another expression.
# - The division between two integers always truncates toward zero.
# - There will not be any division by zero.
# - The input represents a valid arithmetic expression in a reverse polish notation.
# - The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


import math
from typing import List

# O(n)
class Solution:
    # More readable
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operations = ["+", "-", "*", "/"]
    
        for token in tokens:
            if token not in operations:
                stack.append(token)
            elif token in operations: 
                val_2 = int(stack.pop())
                val_1 = int(stack.pop())

                if token == "+":
                    stack.append(val_1 + val_2)
                elif token == "-":
                    stack.append(val_1 - val_2)
                elif token == "*":
                    stack.append(val_1 * val_2)
                elif token == "/":
                    stack.append(val_1 / val_2)

        return math.floor(stack[-1])

    def evalRPNShorter(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]