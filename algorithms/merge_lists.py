from typing import List


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


class Merge2Lists:
    def mergeTwoLists(_, l1: ListNode, l2: ListNode):
        return merge_2_lists(l1, l2)


class MergeKLists:
    def mergeKLists(self, lists: List[ListNode]):
        if not len(lists):
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        left_node = self.mergeKLists(left)
        right_node = self.mergeKLists(right)

        return merge_2_lists(left_node, right_node)
