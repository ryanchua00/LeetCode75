from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse k elements, repeat for each set of k elements.
        # [1,2,3,4,5,6] k=3
        # [3,2,1,6,5,4]

        # if less than 3, dont flip.
        # [1,2,3,4,5] k=3
        # [3,2,1,4,5]

        # copy the list up to k elements
        # [1,2,3,4,5,6] k = 3
        # head -> 1 -> 2 -> 3
        # reverse into head -> 3 -> 2 -> 1

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr:
                print(curr.val)
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        res = ListNode()
        new = ListNode(-1)
        tempNew = new
        curr = res
        count = 0
        while head:
            if count < k:
                node = ListNode(head.val)
                new.next = node
                new = new.next
                count += 1
                head = head.next
            else:
                count = 0
                # reverse
                tmp = new
                reversed = reverse(tempNew.next)
                curr.next = reversed
                curr = tempNew.next
                new = ListNode(-1)
                tempNew = new

        if new and count < k:
            curr.next = tempNew.next
        if new and count == k:
            reversed = reverse(tempNew.next)
            curr.next = reversed

        # return head
        return res.next
