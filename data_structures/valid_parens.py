class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s: str):
        if not len(s):
            return True
        if len(s) % 2:
            return False
        for x in s:
            if not len(self.stack):
                self.stack.append(x)
            else:
                prev_idx = len(self.stack) - 1
                if self.stack[prev_idx] == '(' and x == ')':
                    del self.stack[prev_idx]
                elif self.stack[prev_idx] == '[' and x == ']':
                    del self.stack[prev_idx]
                elif self.stack[prev_idx] == '{' and x == '}':
                    del self.stack[prev_idx]
                else:
                    self.stack.append(x)
        if not len(self.stack):
            return True
        return False
