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


class AbbreviatedWord:
    def __init__(self, s, start, count):
        self.s = s
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    wordLen = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord([], 0, 0))
    while queue:
        abWord = queue.popleft()
        if abWord.start == wordLen:
            if abWord.count != 0:
                abWord.s.append(str(abWord.count))
            result.append(''.join(abWord.s))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            queue.append(AbbreviatedWord(list(abWord.s),
                                         abWord.start + 1, abWord.count + 1))

            # restart abbreviating, append the count and the current character to the string
            if abWord.count != 0:
                abWord.s.append(str(abWord.count))

            newWord = list(abWord.s)
            newWord.append(word[abWord.start])
            queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

    return result


def diff_ways_to_evaluate_expression(input):
    return diff_ways_to_evaluate_expression_rec(input, {})


def diff_ways_to_evaluate_expression_rec(input, map):
    if input in map:
        return map[input]

    result = []

    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
        return result
    for i in range(len(input)):
        char = input[i]
        if not char.isdigit():
            left = diff_ways_to_evaluate_expression_rec(input[:i], map)
            right = diff_ways_to_evaluate_expression_rec(input[i+1:], map)

            for part1 in left:
                for part2 in right:
                    if char == '+':
                        result.append(part1 + part2)
                    elif char == '-':
                        result.append(part1 - part2)
                    elif char == '*':
                        result.append(part1 * part2)
    map[input] = result
    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_rec(1, n)


def find_unique_trees_rec(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_subtrees = find_unique_trees_rec(start, i - 1)
        right_subtrees = find_unique_trees_rec(i + 1, end)

        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)

    return result


def count_unique_trees(n):
    return count_unique_trees_rec(n, {})


def count_unique_trees_rec(n, map):
    if n in map:
        return map[n]
    if n <= 1:
        return 1
    result = 0

    for i in range(1, n + 1):
        count_left_subtrees = count_unique_trees_rec(i - 1, map)
        count_right_subtrees = count_unique_trees_rec(n - i, map)

        result += (count_left_subtrees * count_right_subtrees)

    map[n] = result
    return result
