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
