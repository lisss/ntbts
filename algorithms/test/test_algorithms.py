from algorithms.add_binary import Solution as AddBinary
from algorithms.alien_dict import Solution as AlienDict
from algorithms.meeting_rooms import Solution as MeetingRooms
from algorithms.merge_intervals import Solution as Intervals
from algorithms.merge_lists import ListNode, Merge2Lists, MergeKLists
from algorithms.search_rotated_array import Solution as RotatedArray
from algorithms.three_sum import Solution as ThreeSum


def test_add_binary():
    s = AddBinary()
    assert s.addBinary('11', '1') == '100'
    assert s.addBinary('1010', '1011') == '10101'
    assert s.addBinary('0', '0') == '0'
    assert s.addBinary('1111', '1111') == '11110'
    assert s.addBinary('100', '110010') == '110110'


def test_alient_dict():
    s = AlienDict()

    assert s.isAlienSorted(['', ''],
                           'hlabcdefgijkmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['hello', 'leetcode'],
                           'hlabcdefgijkmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['word', 'world', 'row'],
                           'worldabcefghijkmnpqstuvxyz') is False
    assert s.isAlienSorted(
        ['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') is False
    assert s.isAlienSorted(['app', 'app', 'apple'],
                           'abcdefghijklmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['app', 'app', 'ab'],
                           'abcdefghijklmnopqrstuvwxyz') is False


def test_meeting_rooms():
    s = MeetingRooms()

    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[4, 5], [3, 6], [2, 5]]) == 3
    assert s.minMeetingRooms([[13, 15], [1, 13]]) == 1
    assert s.minMeetingRooms([[1, 5], [8, 9], [8, 9]]) == 2


def test_merge_intervals():
    sb = Intervals()
    assert sb.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sb.merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    assert sb.merge([[4, 4]]) == [[4, 4]]
    assert sb.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert sb.merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert sb.merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert sb.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert sb.merge([[2, 3], [4, 5], [1, 6]]) == [[1, 6]]
    assert sb.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
    assert sb.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
    assert sb.merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]


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


def test_search_rotated_array():
    s = RotatedArray()

    assert s.search([2, 3, 1], 1) == 2
    assert s.search([3, 4, 5, 6, 7, 8, 1, 2], 1) == 6
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([1], 1) == 0
    assert s.search([3, 5, 1], 3) == 0
    assert s.search([5, 1, 3], 5) == 0
    assert s.search([5, 1, 3], 3) == 2
    assert s.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
    assert s.search([6, 7, 1, 2, 3, 4, 5], 6) == 0


def test_three_sum():
    s = ThreeSum()
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([-1, 0, 1, 2, -1, -4, -1]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3],
                                                [-2, 0, 2], [-1, 0, 1]]
