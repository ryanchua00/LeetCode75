# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # value == subroot
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        if root.val == subRoot.val:
            p, q = root, subRoot
            stack = [(p, q)]
            while stack:
                curr_p, curr_q = stack.pop()
                if not curr_p and not curr_q:
                    continue
                elif (not curr_p or not curr_q) or (curr_q.val != curr_p.val):
                    break
                stack.append((curr_p.left, curr_q.left))
                stack.append((curr_p.right, curr_q.right))

        return self.isSubtree(root.left) or self.isSubtree(root.right)
