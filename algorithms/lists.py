from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_2_lists(l1: ListNode, l2: ListNode):
    head = ListNode()
    curr = head
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 is None:
        curr.next = l2
    else:
        curr.next = l1

    return head.next


class Solution:
    def mergeTwoLists(_, l1: ListNode, l2: ListNode):
        return merge_2_lists(l1, l2)

    def mergeKLists(self, lists: List[ListNode]):
        count = 0
        heap = []
        head = ListNode()
        curr = head
        for x in lists:
            if x:
                heapq.heappush(heap, (x.val, count, x))
                count += 1

        while len(heap):
            _, _, next = heapq.heappop(heap)
            curr.next = next
            curr = curr.next
            if next.next:
                heapq.heappush(heap, (next.next.val, count, next.next))
                count += 1
        return head.next

    def deleteDuplicates(self, head: ListNode):
        if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
