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

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

    def minRemoveToMakeValid(self, s: str):
        open, invalid = [], []
        res = ''

        for i, c in enumerate(s):
            if c == '(':
                open.append(i)
            if c == ')':
                if len(open):
                    open.pop()
                else:
                    invalid.append(i)

        invalid += open
        invalid = set(invalid)

        for i, x in enumerate(s):
            if i not in invalid:
                res += x
        return res
