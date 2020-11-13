from algorithms.merge_lists import ListNode, Merge2Lists, MergeKLists


def node_to_list(node: ListNode):
    curr = node
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def test_merge_2_lists():
    s = Merge2Lists()
    assert node_to_list(s.mergeTwoLists(None, None)) == []
    assert node_to_list(s.mergeTwoLists(None, ListNode(0))) == [0]
    assert node_to_list(s.mergeTwoLists(ListNode(1), ListNode(1))) == [1, 1]
    assert node_to_list(s.mergeTwoLists(ListNode(1), ListNode(2))) == [1, 2]
    assert node_to_list(s.mergeTwoLists(ListNode(2), ListNode(1))) == [1, 2]
    assert node_to_list(s.mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4))))) == [1, 1, 2, 3, 4, 4]


def test_merge_k_lists():
    s = MergeKLists()
    assert node_to_list(s.mergeKLists([])) == []
    assert node_to_list(s.mergeKLists([ListNode(1)])) == [1]
    assert node_to_list(s.mergeKLists(
        [ListNode(2), None, ListNode(-1)])) == [-1, 2]
    assert node_to_list(s.mergeKLists(
        [ListNode(2), ListNode(2), ListNode(-1), None])) == [-1, 2, 2]
    assert node_to_list(s.mergeKLists(
        [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
    ) == [1, 1, 2, 3, 4, 4, 5, 6]
