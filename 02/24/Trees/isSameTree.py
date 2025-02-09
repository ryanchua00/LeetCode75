# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check current value,
        # check left...
        if not p and not q:
            return True
        elif not p or not q:
            return False

        stack = [(p, q)]
        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p and not curr_q:
                continue
            elif not curr_p or not curr_q:
                return False
            elif curr_q.val != curr_p.val:
                return False
            stack.append((curr_p.left, curr_q.left))
            stack.append((curr_p.right, curr_q.right))

        return True
