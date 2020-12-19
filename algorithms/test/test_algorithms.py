from algorithms.nums import Nums
from algorithms.alien_dict import Solution as AlienDict
from algorithms.heapq import Solution as HeapQ
from algorithms.intervals import Solution as Intervals
from algorithms.lists import ListNode, Solution as Lists
from algorithms.search_rotated_array import Solution as RotatedArray
from algorithms.three_sum import Solution as ThreeSum
from algorithms.min_window import Solution as Window
from algorithms.trees import Solution as Tree, TreeNode


def test_add_binary():
    s = Nums()
    assert s.addBinary('11', '1') == '100'
    assert s.addBinary('1010', '1011') == '10101'
    assert s.addBinary('0', '0') == '0'
    assert s.addBinary('1111', '1111') == '11110'
    assert s.addBinary('100', '110010') == '110110'


def test_add_one():
    s = Nums()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([0]) == [1]
    assert s.plusOne([9]) == [1, 0]


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
    s = HeapQ()

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


def test_intervals_intersection():
    sb = Intervals()
    assert sb.intervalIntersection(
        [[0, 2], [5, 10], [13, 23],
         [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert sb.intervalIntersection(
        [[4, 11]], [[1, 2], [8, 11], [12, 13], [14, 15], [17, 19]]) == [[8, 11]]


def test_insert_interval():
    s = Intervals()
    assert s.insert([[1, 3], [5, 9]], [2, 5]) == [[1, 9]]
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [
                    4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert s.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]


def node_to_list(node: ListNode):
    curr = node
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def test_merge_2_lists():
    s = Lists()
    assert node_to_list(s.mergeTwoLists(None, None)) == []
    assert node_to_list(s.mergeTwoLists(None, ListNode(0))) == [0]
    assert node_to_list(s.mergeTwoLists(ListNode(1), ListNode(1))) == [1, 1]
    assert node_to_list(s.mergeTwoLists(ListNode(1), ListNode(2))) == [1, 2]
    assert node_to_list(s.mergeTwoLists(ListNode(2), ListNode(1))) == [1, 2]
    assert node_to_list(s.mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4))))) == [1, 1, 2, 3, 4, 4]


def test_merge_k_lists():
    s = Lists()
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


def test_remove_duplicates_from_list():
    s = Lists()
    assert node_to_list(s.deleteDuplicates(None)) == []
    assert node_to_list(s.deleteDuplicates(ListNode(1))) == [1]
    assert node_to_list(s.deleteDuplicates(
        ListNode(1, ListNode(1, ListNode(2))))) == [1, 2]
    assert node_to_list(s.deleteDuplicates(ListNode(1, ListNode(
        1, ListNode(2, ListNode(3, ListNode(3))))))) == [1, 2, 3]


def test_search_rotated_array():
    s = RotatedArray()

    assert s.search([2, 3, 1], 1) == 2
    assert s.search([1, 3], 3) == 1
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

    assert s.search_2([3, 1, 1], 1) is True
    assert s.search_2([1, 1, 3, 1], 3) is True
    assert s.search_2([1, 1, 1, 1, 1, 2, 1], 1) is True
    assert s.search_2([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search_2([2, 5, 6, 0, 0, 1, 2], 3) is False


def test_three_sum():
    s = ThreeSum()
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([-1, 0, 1, 2, -1, -4, -1]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3],
                                                [-2, 0, 2], [-1, 0, 1]]


def test_min_window():
    s = Window()
    assert s.minWindow('a', 'a') == 'a'
    assert s.minWindow('a', 'b') == ''
    assert s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
    assert s.minWindow('ADOBECODEBANCTY', 'ABC') == 'BANC'
    assert s.minWindow('abc', 'b') == 'b'
    assert s.minWindow('cabwefgewcwaefgcf', 'cae') == 'cwae'


def test_kth_smallest_in_bst():
    s = Tree()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    assert s.kthSmallest(root, 1) == 1

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    assert s.kthSmallest(root, 3) == 3

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert s.kthSmallest(root, 2) == 2

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert s.kthSmallest(root, 3) == 3


def test_range_sum_in_bst():
    s = Tree()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    assert s.rangeSumBST(root, 7, 15) == 32

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)
    assert s.rangeSumBST(root, 6, 10) == 23


def test_tree_paths_in_bst():
    s = Tree()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert s.binaryTreePaths(root) == ['1->2->4', '1->2->5', '1->3']


def test_subtree_all_deepest_in_bst():
    s = Tree()

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    assert s.subtreeWithAllDeepest(root).val == 2


def test_max_path_sum_in_bst():
    s = Tree()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert s.maxPathSum(root) == 6

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert s.maxPathSum(root) == 42

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    assert s.maxPathSum(root) == 48


def test_k_closest_points():
    s = HeapQ()

    assert s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert s.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
    assert s.kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]


def test_task_schedule():
    s = HeapQ()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert s.leastInterval(["A", "A", "A", "A", "A",
                            "A", "B", "C", "D", "E", "F", "G"], 2) == 16
