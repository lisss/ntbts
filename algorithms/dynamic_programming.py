import math
from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum


def can_partition(num: List[int]):
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
                dp[i][s] = dp[i - 1][s] or dp[i - 1][s - num[i]]
            else:
                dp[i][s] = dp[i - 1][s]

    return dp[n - 1][target_s]


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
def max_profit(prices: List[int]):
    if len(prices) <= 1:
        return 0

    left_min = prices[0]
    right_max = prices[-1]

    length = len(prices)
    left_profits = [0] * length
    # pad the right DP array with an additional zero for convenience.
    right_profits = [0] * (length + 1)

    # construct the bidirectional DP array
    for l in range(1, length):
        left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
        left_min = min(left_min, prices[l])

        r = length - 1 - l
        right_profits[r] = max(right_profits[r+1], right_max - prices[r])
        right_max = max(right_max, prices[r])

    max_profit = 0
    for i in range(0, length):
        max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

    return max_profit


def max_profit_optimized(prices: List[int]):
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0

    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        # reinvest the gained profit in the second transaction
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)

    return t2_profit


def max_profit_optimized_2(prices: List[int]):
    t1_cost = prices[0]
    t1_profit = 0

    most_money_avail = -prices[0]
    overall_profit = 0

    for curr_price in prices:
        t1_cost = min(t1_cost, curr_price)
        t1_profit = max(t1_profit, curr_price - t1_cost)

        most_money_avail = max(most_money_avail, t1_profit - curr_price)
        overall_profit = max(overall_profit, most_money_avail + curr_price)
    return overall_profit


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
def max_profit_k_tr(k: int, prices: List[int]):
    n = len(prices)

    # solve special cases
    if not prices or k == 0:
        return 0

    if 2*k > n:
        res = 0
        for i, j in zip(prices[1:], prices[:-1]):
            res += max(0, i - j)
        return res

    # dp[i][used_k][ishold] = balance
    # ishold: 0 nothold, 1 hold
    dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

    # set starting value
    dp[0][0][0] = 0
    dp[0][1][1] = -prices[0]

    # fill the array
    for i in range(1, n):
        for j in range(k+1):
            # transition equation
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
            # you can't hold stock without any transaction
            if j > 0:
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

    res = max(dp[n-1][j][0] for j in range(k+1))
    return res


def max_profit_k_tr_2(k: int, prices: List[int]):
    if 2*k >= len(prices):
        return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))

    pnl = [0]*len(prices)
    for _ in range(k):
        val = 0
        for i in range(1, len(pnl)):
            val = max(pnl[i], val + prices[i] - prices[i-1])
            pnl[i] = max(pnl[i-1], val)
    return pnl[-1]


print(max_profit_optimized_2([7, 1, 5, 3, 6, 4]))
