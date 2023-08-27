# Easy — Trees
# Given a binary tree, determine if it is height-balanced

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) >= 0

    def dfs(self, root):
        if not root:
            return 0

        leftLevel = self.dfs(root.left)
        rightLevel = self.dfs(root.right)

        if leftLevel == -1 or rightLevel == -1:
            return -1
        elif abs(leftLevel - rightLevel) > 1:
            return -1

        return 1 + max(leftLevel, rightLevel)

