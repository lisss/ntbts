from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum


def can_partition(self, num: List[int]):
    def can_part_rec(dp: List[List[int]], num: List[int], s, i):
        if s == 0:
            return True

        n = len(num)
        if n == 0 or i >= n:
            return False

        if dp[i][s] != -1:
            return dp[i][s]

        if num[i] <= s:
            can_part = can_part_rec(dp, num, s - num[i], i + 1)
            dp[i][s] = can_part
            if can_part:
                return True

        return can_part_rec(dp, num, s, i + 1)

    total_s = sum(num)
    if total_s % 2 == 1:
        return False

    target_s = total_s // 2

    dp = [[-1 for _ in range(target_s + 1)] for _ in range(len(num))]
    return can_part_rec(dp, num, target_s, 0)


# tbh, it's much slower than bottom-up memoized version
def can_partition_bottom_up(num: List[int]):
    total_s = sum(num)
    if total_s % 2 == 1:
        return False

    target_s = total_s // 2

    dp = [[False for _ in range(target_s + 1)] for _ in range(len(num))]
    n = len(num)

    for i in range(0, n):
        dp[i][0] = True

    for s in range(0, target_s + 1):
        if num[0] == s:
            dp[0][s] = True

    for i in range(1, n):
        for s in range(1, target_s+1):
            if num[i] <= s:
                dp[i % 2][s] = dp[(i - 1) %
                                  2][s] or dp[(i - 1) % 2][s - num[i]]
            else:
                dp[i % 2][s] = dp[(i - 1) % 2][s]

    return dp[(n - 1) % 2][target_s]
