# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return list1
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        res = ListNode()
        if list1.val < list2.val:
            res.next = list1
            list1 = list1.next
        else:
            res.next = list2
            list2 = list2.next

        curr = res.next
        prev = None

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return res
