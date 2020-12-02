# https://leetcode.com/problems/first-bad-version/
def isBadVersion(version):
    pass


class Solution:
    def _do_find(self, start, end):
        mid = start + (end - start) // 2
        is_bad = isBadVersion(mid)
        if start == end:
            return end
        if is_bad:
            return self._do_find(start, mid)
        else:
            return self._do_find(mid + 1, end)

    def firstBadVersion(self, n):
        return self._do_find(1, n)
