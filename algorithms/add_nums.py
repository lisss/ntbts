from typing import List


def add_2_nums(base: int, a: List[int], b: List[int]):
    max_num = a if len(a) >= len(b) else b
    min_num = a if max_num == b else b
    len_diff = len(max_num) - len(min_num)
    start, end = 0, len(max_num) - 1
    res = [0] * (len(max_num) + 1)
    mem = 0
    while start <= end:
        a_val = int(max_num[end])
        b_val = int(min_num[end - len_diff]) if end - len_diff >= 0 else 0
        curr = a_val + b_val + mem
        write = curr % base
        mem = curr // base
        res[end + 1] = write
        end -= 1
    if mem:
        res[0] = mem
    if res[0] == 0:
        del res[0]
    return res


class AddBinary:
    def addBinary(self, a: str, b: str):
        return ''.join([str(x) for x in add_2_nums(2, list(a), list(b))])


class AddOne:
    def plusOne(self, digits: List[int]):
        return add_2_nums(10, digits, [1])
