"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        head = Node()
        queue = [(node, head)]
        while queue:
            curr, prev = queue.pop(0)
            seen.add(curr)
            prev.neighbors.append(Node(curr.val))
            for node in curr.neighbors:
                queue.append((node, curr))

        return head.neighbors[0]
