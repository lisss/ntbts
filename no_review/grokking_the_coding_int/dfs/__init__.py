import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BT path sum (easy)
def has_path(root, s):
    if root.left and root.right:
        s = s - root.val
        return has_path(root.left, s) or has_path(root.right, s)
    else:
        return root.val == s


# All Paths for a Sum (medium)
def find_paths(root, s):
    def _do(root, s, res):
        if not root:
            return

        # curr.append(root.val)

        if not root.left and not root.right and root.val == s:
            # why do they store current path in additional array?
            # res.append(curr)
            res.append(root.val)

        else:
            _do(root.left, s - root.val, res)
            _do(root.right, s - root.val, res)

        # del curr[-1]

    allPaths = []
    _do(root, s, allPaths)
    return len(allPaths)


# Sum of Path Numbers (medium)
def find_sum_of_path_numbers(root):
    def _do(root, sm):
        if not root:
            return 0

        sm = sm * 10 + root.val
        if not root.left and not root.right:
            return sm
        return _do(root.left, sm) + _do(root.right, sm)

    return _do(root, 0)

# Path With Given Sequence (medium)


def find_path(root, sequence):
    def _do(root, curr):
        if not root:
            return False

        len_seq = len(sequence)

        if curr >= len_seq or root.val != sequence[curr]:
            return False
        if not root.left and not root.right:
            return curr == len_seq - 1
        return _do(root.left, curr + 1) or _do(root.right, curr + 1)

    if not root:
        return len(sequence) == 0
    return _do(root, 0)


# Count Paths for a Sum (medium)
def count_paths(root, s):
    def _do(root, curr):
        if not root:
            return 0
        curr.append(root.val)

        curr_sum = 0
        res = 0

        for i in range(len(curr) - 1, -1, -1):
            n = curr[i]
            curr_sum += n
            if curr_sum == s:
                res += 1

        res += _do(root.left, curr)
        res += _do(root.right, curr)

        del curr[-1]
        return res

    return _do(root, [])


# Problem Challenge 1 - Tree Diameter (medium)
class TreeMax:
    def __init__(self):
        self.treeDiameter = 0
        self.max_sum = -math.inf

    def find_diameter(self, root):
        def _do(root):
            if not root:
                return 0

            left = _do(root.left)
            right = _do(root.right)

            diam = left + right + 1
            self.treeDiameter = max(self.treeDiameter, diam)

            return max(left, right) + 1

        _do(root)
        return self.treeDiameter

    # Problem Challenge 2 - Path with Maximum Sum (hard)
    def find_maximum_path_sum(self, root):
        def _do(root):
            if not root:
                return 0

            left = _do(root.left)
            right = _do(root.right)

            maxLeft = max(left, 0)
            maxRight = max(right, 0)

            local_sum = maxLeft + maxRight + root.val

            self.max_sum = max(self.max_sum, local_sum)
            return max(maxLeft, maxRight) + root.val

        _do(root)
        return self.max_sum
