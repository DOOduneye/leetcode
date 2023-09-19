# Easy — Trees
# Given the root of a binary tree, return *its maximum depth*.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right
    
    

class Solution:
    # O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, count):
        if root is None:
            return count

        count += 1

        left_count = self.dfs(root.left, count)
        right_count = self.dfs(root.right, count)

        return max(left_count, right_count)

    # O(n)
    def maxDepthShorter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

