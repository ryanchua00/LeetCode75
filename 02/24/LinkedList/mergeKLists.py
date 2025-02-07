# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # k sorted lists
        # return 1 sorted list

        # Each list has varying length
        # Merge 2 sorted lists into a sorted list -> repeat until 1 sorted list remaining O(mn)
        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]):
            if list1 is None and list2 is None:
                return list1
            elif list1 is None:
                return list2
            elif list2 is None:
                return list1

            head = ListNode()
            curr = head
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            curr.next = list1 or list2

            return head.next

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(merge2Lists(l1, l2))
            lists = mergedLists

        return lists[0]
