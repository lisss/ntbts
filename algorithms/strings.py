# https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, A: str, B: str):
        if len(A) != len(B):
            return False
        swap = []
        sim_chars = set()
        s = 0
        i = 0

        while i < len(A):
            if A[i] not in sim_chars:
                sim_chars.add(A[i])
            else:
                s += 1
            if A[i] != B[i]:
                swap.append((A[i], B[i]))
            i += 1

        if not len(swap) and s > 0:
            return True

        if len(swap) == 1 or len(swap) > 2:
            return False

        if len(swap):
            sa1, sb1 = swap[0]
            sa2, sb2 = swap[1]

            if sa1 == sb2 and sb1 == sa2:
                return True

        return False
