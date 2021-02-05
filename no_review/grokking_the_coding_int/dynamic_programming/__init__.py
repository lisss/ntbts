# bottom-up dynamic programming approach
from __future__ import print_function
from typing import List


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[(n-1) % 2][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[(i - 1) % 2][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


def solve_knapsack_optimized(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    # we only need one previous row to find the optimal solution, overall we need '2' rows
    # the above solution is similar to the previous solution, the only difference is that
    # we use `i % 2` instead of `i` and `(i-1) % 2` instead if `i-1`
    dp = [[0 for x in range(capacity+1)] for y in range(2)]
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
            # exclude the item
            profit2 = dp[(i - 1) % 2][c]
            # take maximum
            dp[i % 2][c] = max(profit1, profit2)

    # print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    return dp[(n - 1) % 2][capacity]


def solve_knapsack_optimized_2(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for _ in range(capacity+1)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            # exclude the item
            profit2 = dp[c]
            # take maximum
            dp[c] = max(profit1, profit2)

    return dp[capacity]


def has_subset(num: List[int], s: int):
    n = len(num)

    def _has_subset_rec(dp: List[List[int]], num: List[int], s: int, i: num):
        if s == 0:
            return True

        if n == 0 or i >= n:
            return False

        if dp[i][s] != -1:
            return dp[i][s]

        if num[i] <= s:
            dp[i][s] = _has_subset_rec(dp, num, s - num[i], i + 1)
            if dp[i][s]:
                return True
        return _has_subset_rec(dp, num, s, i + 1)

    dp = [[-1 for _ in range(s + 1)] for _ in range(len(num))]

    return _has_subset_rec(dp, num, s, 0)


def has_subset_bottom_up(num: List[int], sm: int):
    n = len(num)
    dp = [[False for _ in range(sm + 1)] for _ in range(2)]

    for s in range(sm + 1):
        if num[0] == s:
            dp[0][s] = True

    for i in range(1, n):
        for s in range(1, sm + 1):
            if dp[(i - 1) % 2][s]:
                dp[i % 2][s] = dp[(i - 1) % 2][s]
            elif s >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i % 2][s] = dp[(i - 1) % 2][s - num[i]]
    return dp[(n - 1) % 2][sm]


def has_subset_bottom_up_optimized(num: List[int], sm: int):
    n = len(num)
    dp = [False for _ in range(sm + 1)]

    for s in range(sm + 1):
        if num[0] == s:
            dp[s] = True

    for i in range(1, n):
        for s in range(sm, -1, -1):
            if not dp[s] and num[i] <= s:
                dp[s] = dp[s - num[i]]
    return dp[n - 1]


def minimum_subset_sum_difference(num: List[int]):
    def _min_subset_diff_rec(dp: List[List[int]], s1: int, s2: int, i: int):
        if i == len(num):
            return abs(s1 - s2)

        if dp[i][s1] != -1:
            return dp[i][s1]

        diff1 = _min_subset_diff_rec(dp, num[i] + s1, s2, i + 1)
        diff2 = _min_subset_diff_rec(dp, s1, num[i] + s2, i + 1)

        dp[i][s1] = min(diff1, diff2)
        return dp[i][s1]

    s = sum(num)
    dp = [[-1 for _ in range(s + 1)] for _ in range(len(num))]

    return _min_subset_diff_rec(dp, 0, 0, 0)


def minimum_subset_sum_difference_bottom_up(num: List[int]):
    sm = sum(num)
    mid_sm = sm // 2
    n = len(num)
    dp = [[False for _ in range(mid_sm + 1)] for _ in range(len(num))]

    for i in range(n):
        dp[i][0] = True

    for s in range(mid_sm + 1):
        if num[0] == s:
            dp[0][s] = True

    for i in range(1, n):
        for s in range(1, mid_sm + 1):
            if num[i] <= s:
                dp[i][s] = dp[i - 1][s - num[i]]
            else:
                dp[i][s] = dp[i - 1][s]

    closest_sum = 0
    for s in range(mid_sm, -1, -1):
        if dp[n - 1][s]:
            closest_sum = s
            break

    return abs((sm - closest_sum) - closest_sum)


def minimum_subset_sum_difference_bottom_up_optimized(num: List[int]):
    sm = sum(num)
    mid_sm = sm // 2
    n = len(num)
    dp = [False for _ in range(mid_sm + 1)]

    for s in range(mid_sm + 1):
        if num[0] == s:
            dp[s] = True

    for i in range(1, n):
        for s in range(mid_sm, -1, -1):
            if not dp[s] and num[i] <= s:
                dp[s] = dp[s - num[i]]

    closest_sum = 0
    for s in range(mid_sm, -1, -1):
        if dp[s]:
            closest_sum = s
            break

    return abs((sm - closest_sum) - closest_sum)


def count_subsets(num: List[int], sm: int):
    n = len(num)

    def _count_rec(dp: List[List[int]], s: int, i: int):
        if s == 0:
            return 1

        if n == 0 or i >= n:
            return 0

        if dp[i][s] != -1:
            return dp[i][s]

        sum1 = 0
        if num[i] <= s:
            sum1 = _count_rec(dp, s - num[i], i + 1)
        sum2 = _count_rec(dp, s, i + 1)
        dp[i][s] = sum1 + sum2
        return dp[i][s]

    dp = [[-1 for _ in range(sm + 1)] for _ in range(n)]
    return _count_rec(dp, sm, 0)


def count_subsets_bottom_up(num: List[int], sm: int):
    n = len(num)

    dp = [[0 for _ in range(sm + 1)] for _ in range(2)]

    for i in range(2):
        dp[i][0] = 1

    for s in range(sm + 1):
        if num[0] == s:
            dp[0][s] = 1

    for i in range(1, n):
        for s in range(1, sm + 1):
            dp[i % 2][s] = dp[(i - 1) % 2][s] + dp[(i - 1) % 2][s - num[i]]

    return dp[(n - 1) % 2][sm]


def count_subsets_bottom_up_optimized(num: List[int], sm: int):
    n = len(num)

    dp = [0 for _ in range(sm + 1)]
    dp[0] = 1

    for s in range(1, sm + 1):
        if num[0] == s:
            dp[s] = 1

    for i in range(1, n):
        for s in range(sm, -1, -1):
            if num[i] <= s:
                dp[s] += dp[s - num[i]]

    return dp[sm]


def find_target_subsets(num: List[int], sm: int):
    n = len(num)
    target_sum = (sm + sum(num))//2

    def _find_subsets_rec(dp: List[List[int]], s: int, i: int):
        if s == 0:
            return 1

        if n == 0 or i >= n:
            return 0

        if dp[i][s] != -1:
            return dp[i][s]

        sum1 = 0

        if num[i] <= s:
            sum1 = _find_subsets_rec(dp, s - num[i], i + 1)
        sum2 = _find_subsets_rec(dp, s, i + 1)

        dp[i][s] = sum1 + sum2
        return dp[i][s]

    dp = [[-1 for _ in range(target_sum + 1)] for _ in range(n)]

    return _find_subsets_rec(dp, target_sum, 0)


def find_target_subsets_bottom_up(num: List[int], sm: int):
    n = len(num)
    target_sum = (sm + sum(num))//2

    dp = [[0 for _ in range(target_sum + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for s in range(target_sum + 1):
        if num[0] == s:
            dp[0][s] = 1

    for i in range(n):
        for s in range(target_sum + 1):
            dp[i][s] = dp[i - 1][s]
            if num[i] <= s:
                dp[i][s] += dp[i - 1][s - num[i]]

    return dp[n - 1][target_sum]


def find_target_subsets_bottom_up_optimized(num: List[int], sm: int):
    n = len(num)
    target_sum = (sm + sum(num))//2

    dp = [0 for _ in range(target_sum + 1)]
    dp[0] = 1

    for s in range(1, target_sum + 1):
        if num[0] == s:
            dp[s] = 1

    for i in range(1, n):
        for s in range(target_sum, -1, -1):
            if num[i] <= s:
                dp[s] += dp[s - num[i]]

    return dp[target_sum]
