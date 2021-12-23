import math
from heapq import *
from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists: List[ListNode]):
    min_heap = []

    for root in lists:
        if root:
            heappush(min_heap, root)

    head, tail = None, None
    while min_heap:
        node = heappop(min_heap)

        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next
        if node.next:
            heappush(min_heap, node.next)

    return head


def find_Kth_smallest(lists: List[List[int]], k: int):
    number = -1
    min_heap = []

    for i in range(len(lists)):
        lst = lists[i]
        if len(lst):
            heappush(min_heap, (lst[0], i, 0))

    count = 1
    while min_heap:
        el, arr_idx, el_idx = heappop(min_heap)
        if count == k:
            return el

        if el_idx + 1 < len(lists[arr_idx]):
            heappush(
                min_heap, (lists[arr_idx][el_idx + 1], arr_idx, el_idx + 1)
            )
        count += 1
    return number


def find_Kth_smallest_matrix(matrix: List[List[int]], k: int):
    number = -1
    min_heap = []

    # we don't need to push more than 'k' elements in the heap
    # since the matrix is sorted
    for i in range(min(k, len(matrix))):
        lst = matrix[i]
        if len(lst):
            heappush(min_heap, (lst[0], i, 0))

    count = 1
    while min_heap:
        el, arr_idx, el_idx = heappop(min_heap)
        if count == k:
            return el

        if el_idx + 1 < len(matrix[arr_idx]):
            heappush(
                min_heap, (matrix[arr_idx][el_idx + 1], arr_idx, el_idx + 1)
            )
        count += 1
    return number


def find_smallest_range(lists: List[List[int]]):
    start, end = 0, math.inf
    curr_max_number = -math.inf
    min_heap = []

    for i in range(len(lists)):
        lst = lists[i]
        if len(lst):
            heappush(min_heap, (lst[0], i, 0))
            curr_max_number = max(curr_max_number, lst[0])

    while len(min_heap) == len(lists):
        el, arr_idx, el_idx = heappop(min_heap)
        if end - start > curr_max_number - el:
            start = el
            end = curr_max_number

        if el_idx + 1 < len(lists[arr_idx]):
            heappush(
                min_heap, (lists[arr_idx][el_idx + 1], arr_idx, el_idx + 1)
            )
            curr_max_number = max(curr_max_number, lists[arr_idx][el_idx + 1])

    return [start, end]


def find_k_largest_pairs(nums1: List[int], nums2: List[int], k: int):
    result = []
    min_heap = []

    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            sm = nums1[i] + nums2[j]

            if len(min_heap) < k:
                heappush(min_heap, (sm, i, j))
            else:
                if sm < min_heap[0][0]:
                    break
                heappop(min_heap)
                heappush(min_heap, (sm, i, j))

    for _, i, j in min_heap:
        result.append([nums1[i], nums2[j]])

    return result


print(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
print(find_k_largest_pairs([5, 2, 1], [2, -1], 3))
