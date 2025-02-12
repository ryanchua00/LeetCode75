# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        # bfs
        queue = [(root, "root", -1)]
        while queue:
            curr, flag, prev = root.pop(0)
            if not curr:
                continue
            if flag == "root":
                queue.append((root.left, "left", curr.val))
                queue.append((root.right, "right", curr.val))
            elif flag == "left":
                if curr.val >= prev:
                    return False
                queue.append((curr.left, "left", curr.val))
                queue.append((curr.right, "right", curr.val))
            else:
                if curr.val <= prev:
                    return False
                queue.append((curr.left, "left", curr.val))
                queue.append((curr.right, "right", curr.val))

        return True
