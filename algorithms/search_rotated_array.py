from typing import List


def search_pivot(nums: List[int], left: int, right: int, piv: int):
    if left == right:
        return piv

    mid = left + (right - left) // 2
    num_left, num_mid, num_right = nums[left], nums[mid], nums[right]

    if num_left < num_right:
        return piv

    if num_mid > num_right:
        piv = mid
        return search_pivot(nums, mid + 1, right, piv)
    return search_pivot(nums, left, mid, piv)


def search_num(nums: List[int], left: int, right: int, piv: int, target: int):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    num_mid = nums[mid]

    if num_mid == target:
        return mid

    if num_mid > target:
        return search_num(nums, left, mid - 1, piv, target)
    return search_num(nums, mid + 1, right, piv, target)


class Solution:
    def search(self, nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        pivot = search_pivot(nums, left, right, right)

        if target > nums[pivot]:
            return -1

        if target >= nums[0]:
            right = pivot
        else:
            left = pivot + 1

        return search_num(nums, left, right, pivot, target)
