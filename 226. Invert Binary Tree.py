# Easy — Trees
# Given the root of a binary tree, invert the tree, and return its root.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        swap = root.left
        root.left = root.right
        root.right = swap

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

