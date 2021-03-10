import math
from typing import List


def binary_search(arr: List[int], key: int):
    start, end = 0, len(arr) - 1
    is_asc = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid

        if is_asc:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def search_ceiling_of_a_number(arr: List[int], key: int):
    start, end = 0, len(arr) - 1
    if arr[end] < key:
        return -1

    while start <= end:
        mid = start + (end - start) // 2
        mid_num = arr[mid]

        if key == mid_num:
            return mid

        if key > mid_num:
            start = mid + 1
        else:
            end = mid - 1

    return start


def search_next_letter(letters, key):
    n = len(letters)
    start, end = 0, n - 1
    if key < letters[0] or key > letters[n - 1]:
        return letters[0]

    while start <= end:
        mid = start + (end - start) // 2

        if key >= letters[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return letters[start % n]


def find_range(arr, key):
    result = [- 1, -1]

    def _do(find_max):
        start, end = 0, len(arr) - 1
        key_idx = -1

        while start <= end:
            mid = start + (end - start) // 2
            mid_num = arr[mid]

            if key > mid_num:
                start = mid + 1
            elif key < mid_num:
                end = mid - 1
            else:
                key_idx = mid
                if find_max:
                    start = mid + 1
                else:
                    end = mid - 1
        return key_idx

    result[0] = _do(False)
    if result[0] != -1:
        result[1] = _do(True)
    return result


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        new_start = end + 1
        end = (end - start + 1) * 2
        start = new_start

    while start <= end:
        mid = start + (end - start) // 2
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:
            return mid
    return -1
