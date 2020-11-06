from typing import List


def find_sum(start, end, target_sum, lst, triplets):
    while start < end:
        curr_sum = lst[start] + lst[end]
        if curr_sum == target_sum:
            res = [-target_sum, lst[start], lst[end]]
            triplets.append(res)
            start += 1
            end -= 1
            # skip duplicates
            while start < end and lst[start] == lst[start - 1]:
                start += 1
            while start < end and lst[end] == lst[end + 1]:
                end -= 1
        if curr_sum > target_sum:
            end -= 1
        if curr_sum < target_sum:
            start += 1


class Solution:
    def threeSum(self, nums: List[int]):
        triplets = []
        end = len(nums) - 1

        nums = sorted(nums)

        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            find_sum(i + 1, end, -nums[i], nums, triplets)

        return triplets
