# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # assume linked list is ordered.
        # 0 > 1 > 2 > 3 > 4 > 5 > 6
        # 0 > 6 > 1 > 5 > 2 > 4 > 3
        # 0 >   > 1 >   > 2 >   > 3
        #     6 >     5 >     4

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        def reverse(list1: ListNode):
            curr = list1
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        second = reverse(slow.next)
        first = head
        # interweave
        # 0 > 1 > 2 > 3
        #     ^
        # 6 > 5 > 4
        #     ^
        # 0 > 6 > 1

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return


solution = Solution()
n1 = ListNode(4)
n2 = ListNode(3, n1)
n3 = ListNode(2, n2)
n4 = ListNode(1, n3)
solution.reorderList(n4)
print(n4.val)
print(n4.next.val)
print(n4.next.next.val)
print(n4.next.next.next.val)
