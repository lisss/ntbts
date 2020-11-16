import math
from collections import deque


# 1. Pair with Target Sum (easy)
def pair_with_targetsum(arr, target_sum):
    start, end = 0, len(arr) - 1

    while start != end:
        current_sum = arr[start] + arr[end]
        if current_sum == target_sum:
            return [start, end]
        elif current_sum < target_sum:
            start += 1
        else:
            end -= 1
    return [-1, -1]


def pair_with_targetsum_2(arr, target_sum):
    nums = {}

    for i, x in enumerate(arr):
        if target_sum - x in nums:
            return [nums[target_sum - x], i]
        else:
            nums[x] = i
    return [-1, -1]


# 2. Remove Duplicates (easy)
def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def remove_element(arr, key):
    next_el = 0

    for x in arr:
        if x != key:
            arr[next_el] = x
            next_el += 1

    return next_el


# 3. Squaring a Sorted Array (easy)
def make_squares(arr):
    n = len(arr)
    squares = [0 for i in range(n)]
    left, right = 0, n - 1
    max_sq_num = n - 1

    while left <= right:
        sq_left = arr[left] ** 2
        sq_right = arr[right] ** 2

        if sq_left > sq_right:
            squares[max_sq_num] = sq_left
            left += 1
        else:
            squares[max_sq_num] = sq_right
            right -= 1
        max_sq_num -= 1

    return squares


# 4. Triplet Sum to Zero (medium)
def search_triplets(arr):
    arr = sorted(arr)
    triplets = []
    for i in range(len(arr)):
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets


def search_pair(arr, target_sum, start, triplets):
    end = len(arr) - 1

    while start < end:
        current_sum = arr[start] + arr[end]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[start], arr[end]])
            start += 1
            end -= 1
            while start < end and arr[start] == arr[start - 1]:
                start += 1  # skip same element to avoid duplicate triplets
            while start < end and arr[end] == arr[end + 1]:
                end -= 1  # skip same element to avoid duplicate triplets
        elif current_sum < target_sum:
            start += 1
        else:
            end -= 1


# Triplet Sum Close to Target (medium)
def triplet_sum_close_to_target(arr, target_sum):
    arr = sorted(arr)

    smallest_diff = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return target_sum

            if (abs(target_diff) < abs(smallest_diff) or
                    (abs(target_diff) == abs(smallest_diff) and
                     target_diff > smallest_diff)):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_diff


# Triplets with Smaller Sum (medium)
def triplet_with_smaller_sum(arr, target_sum):
    arr = sorted(arr)
    count = 0
    for i in range(len(arr)):
        count += search_pair_2(arr, target_sum - arr[i], i)
    return count


def search_pair_2(arr, target_sum, start):
    left, right = start + 1, len(arr) - 1
    count = 0

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum < target_sum:
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            count += right - left
            left += 1
        else:
            right -= 1
    return count


def triplet_with_smaller_sum_1(arr, target_sum):
    arr = sorted(arr)
    triplets = []
    for i in range(len(arr)):
        search_pair_2_1(arr, target_sum - arr[i], i, triplets)
    return triplets


def search_pair_2_1(arr, target_sum, start, triplets):
    left, right = start + 1, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum < target_sum:
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            for i in range(right, left, -1):
                triplets.append([arr[start], arr[left], arr[i]])
            left += 1
        else:
            right -= 1


# IT'S COMPLICATED
# Subarrays with Product Less than a Target (medium)
def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


# Dutch National Flag Problem (medium)
def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0

    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1

    return arr


# Problem Challenge 1 - Quadruple Sum to Target (medium)
def search_quadruplets(arr, target):
    quadruplets = []
    arr = sorted(arr)
    for i in range(len(arr) - 3):
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > 0 and arr[j] == arr[j - 1]:
                continue
            search_pair_q(arr, target, i, j, quadruplets)
    return quadruplets


def search_pair_q(arr, target_sum, first, second, quadruplets):
    left, right = second + 1, len(arr) - 1

    while left < right:
        current_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if current_sum == target_sum:
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


# Problem Challenge 2 - Comparing Strings containing Backspaces (medium)
def backspace_compare(str1: str, str2: str):
    id1 = len(str1) - 1
    id2 = len(str2) - 1

    while id1 >= 0 or id2 >= 0:
        next_id1 = get_next(str1, id1)
        next_id2 = get_next(str2, id2)
        if next_id1 < 0 and next_id2 < 0:
            return True
        if next_id1 < 0 or next_id2 < 0:
            return False
        if str1[next_id1] != str2[next_id2]:
            return False
        id1 = next_id1 - 1
        id2 = next_id2 - 1

    return True


def get_next(st, i):
    to_skip = 0

    while i >= 0:
        if st[i] == '#':
            to_skip += 1
        elif to_skip > 0:
            to_skip -= 1
        else:
            break
        i -= 1
    return i


# INCORRECT SOLUTION
# Problem Challenge 3 - Minimum Window Sort (medium)
def shortest_window_sort(arr):
    left, right = 0, len(arr) - 1
    start, end = math.inf, 0

    while left < right:
        if arr[left] > arr[left + 1]:
            start = left
            if end:
                return end - left + 1
        if arr[right] < arr[right - 1] or arr[right - 1] < arr[left]:
            end = right
            if start < math.inf:
                return right - start + 1
        left += 1
        right -= 1
    return 0


def main():
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))


main()
