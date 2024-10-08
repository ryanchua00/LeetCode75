# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2  
        if list2 is None:
            return list1 
        head = ListNode()
        node = ListNode()
        index = 0
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            if index == 0:
                head = node
            node = node.next
            index += 1

        if list1 is None and list2 is not None:
            node.next = list2

        if list2 is None and list1 is not None:
            node.next = list1

        return head.next
# list1 = [1,2,4]
#              ^
# list2 = [1,3,4]
#            ^
#           l2 l1 l1
# node = [0, 1, 1, 2]
# head =  ^ 
