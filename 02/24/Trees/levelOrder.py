# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        # BFS
        level = 0
        queue = [(root, level)]
        levelOrder = []
        while queue:
            curr, level = queue.pop(0)
            if not curr:
                continue
            if len(levelOrder) == level:
                levelOrder.append([curr.val])
            else:
                levelOrder[level].append(curr.val)

            queue.append((curr.left, level + 1))
            queue.append((curr.right, level + 1))

        return levelOrder
