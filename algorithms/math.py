class Solution:
    # https://leetcode.com/problems/powx-n/
    def myPow(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        i, j = divmod(n, 2)
        if n > 0:
            res = self.myPow(x, i)
            if j:
                return x * res * res
            return res * res
        return 1 / self.myPow(x, -n)
