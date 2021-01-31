from typing import List


class Solution:
    def combine(self, n: int, k: int):
        res = []

        def backtrack(first: int, curr: List[int]):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return res

    # very strange solution, i would never deduce it
    def combine1(self, n: int, k: int):
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]

        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output
