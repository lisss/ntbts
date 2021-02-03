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
