from typing import List


def cyclic_sort(nums: List[int]):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


def find_missing_number(nums: List[int]):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i

    return n


def find_missing_numbers(nums: List[int]):
    missingNumbers = []
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            missingNumbers.append(i + 1)

    return missingNumbers


def find_duplicate(nums: List[int]):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != i + 1:
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


def find_duplicate_fast_slow(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cycleLength = 1
    while current != arr[slow]:
        current = arr[current]
        cycleLength += 1

    return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while cycleLength > 0:
        pointer2 = arr[pointer2]
        cycleLength -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


def find_all_duplicates(nums: List[int]):
    duplicate_numbers = []
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


def find_corrupt_numbers(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return [nums[i], i + 1]
    return [-1, -1]


def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return -1


def find_first_k_missing_positive(nums, k):
    missing_numbers = []
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k and i + 1 != nums[i]:
            missing_numbers.append(i + 1)
            extra_numbers.add(nums[i])

    i = 1
    while len(missing_numbers) < k:
        next_num = i + n
        if next_num not in extra_numbers:
            missing_numbers.append(next_num)
        i += 1

    return missing_numbers
