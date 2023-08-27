# Easy — Trees
# Given the root of a binary tree, return the inorder traversal of its nodes values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root, path):
            if not root:
                return

            traversal(root.left, path)
            path.append(root.val)
            traversal(root.right, path)

            return path

        return traversal(root, [])
