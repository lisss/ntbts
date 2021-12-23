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


def search_min_diff_element(arr, key):
    n = len(arr) - 1

    if not len(arr):
        return -1
    if key >= arr[n]:
        return arr[n]
    if key <= arr[0]:
        return arr[0]

    start, end = 0, n
    while start <= end:
        mid = start + (end - start) // 2
        mid_num = arr[mid]

        if key == mid_num:
            return mid_num
        if key > mid_num:
            start = mid + 1
        else:
            end = mid - 1
    start_num, end_num = arr[start], arr[end]
    return start_num if abs(start_num - key) < abs(end_num - key) else end_num


def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]


def search_bitonic_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        if arr[mid] > arr[mid + 1]:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid
        if arr[start] == arr[mid] == arr[end]:
            start += 1
            end -= 1

        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def count_rotations(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # this is the only difference from the previous solution
        # if numbers at indices start, mid, and end are same, we can't choose a side
        # the best we can do is to skip one number from both ends
        # if they are not the smallest number
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:  # if element at start+1 is not the smallest
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:  # if the element at end is not the smallest
                return end
            end -= 1
        # left side is sorted, so the pivot is on right side
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1
    return 0


print(count_rotations([10, 15, 1, 3, 8]))
print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
print(count_rotations([1, 3, 8, 10]))
print(count_rotations([2, 3, 8, 10, 12, 13, 14, 1]))
