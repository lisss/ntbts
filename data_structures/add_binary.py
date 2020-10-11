BASE = 2


class Solution:
    def addBinary(self, a: str, b: str):
        max_num = a if len(a) >= len(b) else b
        min_num = a if max_num == b else b
        len_diff = len(max_num) - len(min_num)
        start, end = 0, len(max_num) - 1
        res = ['0'] * (len(max_num) + 1)
        while start <= end:
            a_val = int(max_num[end])
            b_val = int(min_num[end - len_diff]) if end - len_diff >= 0 else 0
            curr = a_val + b_val + int(res[end + 1])
            write = curr % BASE
            mem = curr // BASE
            res[end + 1] = str(write)
            if mem > 0:
                res[end] = str(mem)
            end -= 1
        if res[0] == '0':
            del res[0]
        return ''.join(res)
