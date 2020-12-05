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


def search_pivot_2(nums: List[int], left: int, right: int):
    if left == right:
        return right

    mid = left + (right - left) // 2
    num_left, num_mid = nums[left], nums[mid]

    if nums[mid] > nums[mid+1]:
        return mid

    if num_mid == num_left:
        return search_pivot_2(nums, left + 1, right)

    if num_mid > num_left:
        return search_pivot_2(nums, mid, right)
    return search_pivot_2(nums, left, mid)


def search_num_2(nums: List[int], left: int, right: int, piv: int, target: int):
    if left > right:
        return False

    mid = left + (right - left) // 2
    num_mid = nums[mid]

    if num_mid == target:
        return True

    if num_mid > target:
        return search_num_2(nums, left, mid - 1, piv, target)
    return search_num_2(nums, mid + 1, right, piv, target)


class Solution:
    # https://leetcode.com/problems/search-in-rotated-sorted-array/
    def search(self, nums: List[int], target: int):
        if not len(nums):
            return -1

        left, right = 0, len(nums) - 1
        pivot = search_pivot(nums, left, right, right)

        if target > nums[pivot]:
            return -1

        if target >= nums[0]:
            right = pivot
        else:
            left = pivot + 1

        return search_num(nums, left, right, pivot, target)

    #  https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    def search_2(self, nums: List[int], target: int):
        if not len(nums):
            return False

        left, right = 0, len(nums) - 1
        pivot = search_pivot_2(nums, left, right)

        if target > nums[pivot]:
            return False

        if target >= nums[0]:
            right = pivot
        else:
            left = pivot + 1

        return search_num_2(nums, left, right, pivot, target)
