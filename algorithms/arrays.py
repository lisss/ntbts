from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]):
        curr_sum = 0
        max_sum = -float('inf')

        for x in nums:
            curr_sum = x + curr_sum if x + curr_sum > x else x
            max_sum = max(curr_sum, max_sum)

        return max_sum

    # https://leetcode.com/problems/merge-sorted-array/
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        a, b, i = m - 1, n - 1, len(nums1) - 1

        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1

        while a > 0:
            nums1[i] = nums1[a]
            a -= 1
            i -= 1
        while b >= 0:
            nums1[i] = nums2[b]
            b -= 1
            i -= 1

        return nums1
