from typing import List
import math


class Solution:
    # https://leetcode.com/problems/buddy-strings/
    def buddyStrings(self, A: str, B: str):
        if len(A) != len(B):
            return False
        swap = []
        sim_chars = set()
        s = 0
        i = 0

        while i < len(A):
            if A[i] not in sim_chars:
                sim_chars.add(A[i])
            else:
                s += 1
            if A[i] != B[i]:
                swap.append((A[i], B[i]))
            i += 1

        if not len(swap) and s > 0:
            return True

        if len(swap) == 1 or len(swap) > 2:
            return False

        if len(swap):
            sa1, sb1 = swap[0]
            sa2, sb2 = swap[1]

            if sa1 == sb2 and sb1 == sa2:
                return True

        return False

    # https://leetcode.com/problems/group-shifted-strings/
    def groupStrings(self, strings: List[str]):
        def _get_key(s: str):
            res = []
            for i in range(len(s) - 1):
                x = (ord(s[i + 1]) - ord(s[i])) % 26
                res.append(x)
            return tuple(res)

        grouped = {}
        for x in strings:
            key = _get_key(x)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(x)

        return [x for x in grouped.values()]

    # https://leetcode.com/problems/simplify-path/
    def simplifyPath(self, path: str):
        res = []

        spl = path.split('/')
        for x in spl:
            if not x or x == '.':
                continue
            if x == '..':
                if len(res):
                    res.pop()
            else:
                res.append(x)

        return '/' + '/'.join(res)

    # https://leetcode.com/problems/custom-sort-string/
    def customSortString(self, S: str, T: str):
        order_map = {}
        res = []

        for c in T:
            if c in order_map:
                order_map[c] += 1
            else:
                order_map[c] = 1

        for x in S:
            if x in order_map:
                res.append(x * order_map[x])

        for x in order_map.keys():
            if x not in S:
                res.append(x * order_map[x])

        return ''.join(res)
