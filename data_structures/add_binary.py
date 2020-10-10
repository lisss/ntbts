class AddBinarySolution:
    def addBinary(self, a: str, b: str):
        mem = 0
        max_num = a if len(a) >= len(b) else b
        min_num = a if max_num == b else b
        len_diff = len(max_num) - len(min_num)
        start, end = 0, len(max_num) - 1
        res = ['0'] * (len(max_num) + 1)
        while start <= end:
            a_val = max_num[end]
            b_val = min_num[end - len_diff] if end - len_diff >= 0 else '0'
            if a_val != b_val:
                if mem == 0:
                    res[end + 1] = '1'
                else:
                    res[end + 1] = '0'
                    mem = 1
            elif a_val == '0' and b_val == '0':
                res[end + 1] = '0' if mem == 0 else '1'
                mem = 0
            else:
                res[end + 1] = '0' if mem == 0 else '1'
                mem = 1
            end -= 1
        if mem == 1:
            res[end + 1] = '1'
        if res[0] == '0':
            del res[0]
        return ''.join(res)
