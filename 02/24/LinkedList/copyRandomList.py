"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # list, make a deep copy
        # iterating once to make the list
        # iterating another time to set random
        # How can you set random if your pointer is not currently at that node?
        # Assuming values are unique, we can hash val - node
        # Values are not unique XXXXX
        nodeMap = {}
        newList = Node(0)
        dummy = newList

        # make list
        # 3 -> 2 -> 1
        #              ^
        # [] -> 3 -> 2 -> 1
        tempHead = head
        tempNew = newList
        while tempHead:
            newVal = Node(tempHead.val)
            if tempHead.val not in nodeMap:
                nodeMap[tempHead.val] = [(newVal, tempHead)]
            else:
                nodeMap[tempHead.val].append((newVal, tempHead))
            tempNew.next = newVal
            tempNew = tempNew.next
            tempHead = tempHead.next

        # set random
        tempHead = head
        tempNew = newList.next
        while tempHead:
            if tempHead.random:
                for node in nodeMap[tempHead.random.val]:
                    if node[1] == tempHead.random:
                        tempNew.random = node[0]
            tempHead = tempHead.next
            tempNew = tempNew.next

        return dummy.next
