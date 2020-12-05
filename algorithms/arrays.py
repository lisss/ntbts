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

    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    def removeDuplicates(self, nums: List[int]):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        j = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[len(nums) - 1]
        j += 1
        return j

    # https://leetcode.com/problems/move-zeroes/
    def moveZeroes(self, nums: List[int]):
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j += 1

        return nums

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    def maxProfit(self, prices: List[int]):
        buy_price = None
        profit = 0

        for i in range(len(prices)):
            curr = prices[i]
            if buy_price is None:
                buy_price = curr
                continue
            if curr > buy_price:
                profit = max(profit, curr - buy_price)
            else:
                buy_price = curr

        return profit

    # https://leetcode.com/problems/rotate-array/
    def rotate(self, nums: List[int], k: int):
        copy = []
        start, end = 0, len(nums)
        k = k if k <= len(nums) else k - len(nums)
        mid = len(nums) - k

        while mid < end:
            copy.append(nums[mid])
            mid += 1

        mid = len(nums) - k
        while start < mid:
            copy.append(nums[start])
            start += 1

        start = 0
        while start < end:
            nums[start] = copy[start]
            start += 1
