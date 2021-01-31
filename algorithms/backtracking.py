class Solution:
    # https://leetcode.com/problems/remove-invalid-parentheses/
    def removeInvalidParentheses(self, s: str):
        res = {}

        left_disc, right_disc = 0, 0
        for ch in s:
            if ch == '(':
                left_disc += 1
            if ch == ')':
                if left_disc:
                    left_disc -= 1
                else:
                    right_disc += 1

        def backtrack(i, curr, left, right, left_rem, right_rem):
            if i == len(s):
                if left_rem == 0 and right_rem == 0:
                    res[''.join(curr)] = 1
            else:
                ch = s[i]
                if ch == '(' and left_rem:
                    backtrack(i + 1, curr, left, right,
                              left_rem - 1, right_rem)
                if ch == ')' and right_rem:
                    backtrack(i + 1, curr, left, right,
                              left_rem, right_rem - 1)
                curr.append(ch)

                if ch != '(' and ch != ')':
                    backtrack(i + 1, curr, left, right,
                              left_rem, right_rem)

                elif ch == '(':
                    backtrack(i + 1, curr, left + 1, right,
                              left_rem, right_rem)
                elif ch == ')' and left > right:
                    backtrack(i + 1, curr, left, right + 1,
                              left_rem, right_rem)

                curr.pop()

        backtrack(0, [], 0, 0, left_disc, right_disc)

        return list(res.keys())
