class Solution:
    def __init__(self):
        self.num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str):
        res = 0
        for i, x in enumerate(s):
            curr = self.num_map[x]
            res += curr
            prev = s[i - 1] if i else None
            if prev:
                if prev == 'I' and x in ['V', 'X']:
                    res -= 2
                elif prev == 'X' and x in ['L', 'C']:
                    res -= 20
                elif prev == 'C' and x in ['D', 'M']:
                    res -= 200
        return res


s = Solution()
print(s.romanToInt('III'))  # 3
print(s.romanToInt('IV'))  # 4
print(s.romanToInt('IX'))  # 9
print(s.romanToInt('LVIII'))  # 58
print(s.romanToInt('XL'))  # 40
print(s.romanToInt('MCMXCIV'))  # 1994
