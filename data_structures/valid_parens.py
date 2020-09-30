open_par = ['(', '[', '{']
closing_par = [')', ']', '}']


class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s: str):
        if not len(s):
            return True
        if len(s) % 2:
            return False
        for x in s:
            if x in open_par:
                self.stack.append(x)
            else:
                if x in closing_par and not len(self.stack):
                    return False
                prev = self.stack[-1]
                if prev == '(' and x == ')':
                    del self.stack[-1]
                elif prev == '[' and x == ']':
                    del self.stack[-1]
                elif prev == '{' and x == '}':
                    del self.stack[-1]
                else:
                    return False
        if not len(self.stack):
            return True
        return False
