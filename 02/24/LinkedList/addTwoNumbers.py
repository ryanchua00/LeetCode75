# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # two linked list, containing an integer in reverse order
        # l1 -> 1 -> 2 -> 3 => 321
        # l2 -> 4 -> 5 -> 6 => 654
        # 321+654 = 975
        # res -> 5 -> 7 -> 9

        # handle cases where l1 l2 diff len
        # l1 -> 3 -> 1
        # l2 -> 4 -> 5 -> 6
        # res -> 7 -> 6 -> 6

        # addition
        # when sum > 10, carry 1 to next value.
        carry = 0
        res = ListNode()
        head = res
        while l1 or l2:
            # add
            if l1 and l2:
                sum = l1.val + l2.val + carry
            elif l1:
                sum = l1.val + carry
            else:
                sum = l2.val + carry

            # check for sum > 10
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0

            # create the node
            node = ListNode(sum)
            res.next = node
            res = res.next

            # move pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            res.next = ListNode(1)

        return head.next
