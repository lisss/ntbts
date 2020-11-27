from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]):
        curr_sum = 0
        max_sum = -float('inf')

        for x in nums:
            curr_sum = x + curr_sum if x + curr_sum > x else x
            max_sum = max(curr_sum, max_sum)

        return max_sum
