from collections import deque


def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number
        # in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set1 = list(subsets[i])
            set1.append(currentNumber)
            subsets.append(set1)

    return subsets


def find_subsets_with_duplicates(nums):
    subsets = []
    nums = sorted(nums)
    subsets.append([])

    for i in range(len(nums)):
        num = nums[i]
        n = len(subsets)
        start = 0
        if i and nums[i - 1] == num:
            start = i
        for j in range(start, n):
            set1 = list(subsets[j])
            set1.append(num)
            subsets.append(set1)
    return subsets


def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])

    for num in nums:
        n = len(permutations)
        for _ in range(n):
            old_perm = permutations.popleft()
            for j in range(len(old_perm) + 1):
                new_perm = list(old_perm)
                new_perm.insert(j, num)

                if len(new_perm) == len(nums):
                    result.append(new_perm)
                else:
                    permutations.append(new_perm)
    return result


def find_letter_case_string_permutations(s: str):
    permutations = []
    permutations.append(s)

    for i in range(len(s)):
        if not s[i].isalpha():
            continue
        n = len(permutations)
        for j in range(n):
            new_s = list(permutations[j])
            new_s[i] = new_s[i].swapcase()
            permutations.append(''.join(new_s))

    return permutations


class ParenthesisStr:
    def __init__(self, s, open_count, close_count):
        self.s = s
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesisStr('', 0, 0))

    while queue:
        ps = queue.popleft()
        if ps.open_count == ps.close_count == num:
            result.append(ps.s)
        if ps.open_count < num:
            queue.append(ParenthesisStr(
                ps.s + '(', ps.open_count + 1, ps.close_count))
        if ps.close_count < ps.open_count:
            queue.append(ParenthesisStr(
                ps.s + ')', ps.open_count, ps.close_count + 1))
    return result
