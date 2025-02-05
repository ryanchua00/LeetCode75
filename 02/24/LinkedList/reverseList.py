# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


solution = Solution()
n1 = ListNode(1)
n2 = ListNode(2, n1)
n3 = ListNode(3, n2)
n4 = ListNode(4, n3)
newHead = solution.reverseList(n4)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)
print(newHead.next.next.next.val)
