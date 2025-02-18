# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def pathSum(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0

            leftMax = max(pathSum(curr.left), 0)
            rightMax = max(pathSum(curr.right), 0)

            res[0] = max(res[0], leftMax + rightMax + curr.val)

            return curr.val + max(leftMax, rightMax)
        maxSum = pathSum(root)

        return max(pathSum(root), res[0])
