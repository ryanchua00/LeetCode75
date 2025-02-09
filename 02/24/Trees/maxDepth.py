# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS, keep track of distance
        if not root:
            return 0
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            node, length = stack.pop()
            maxDepth = max(length, maxDepth)
            if node.left:
                stack.append((root.left, length + 1))
            if node.right:
                stack.append((root.right, length + 1))

        return maxDepth
