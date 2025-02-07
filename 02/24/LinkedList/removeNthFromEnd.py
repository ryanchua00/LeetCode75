# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse, remove, reverse O(n)
        # n === len(list) or n === 1
        # 1 > 2 > .... > x - 1 > x

        # 1   2 > 3
        # ^c  ^t
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        newHead = prev
        if n == 1:
            newHead = newHead.next
        else:
            # 3 > 2 > 1, n = 2
            distance = n - 2
            while distance > 0:
                distance -= 1
                prev = prev.next
            prev.next = prev.next.next

        curr = newHead
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
