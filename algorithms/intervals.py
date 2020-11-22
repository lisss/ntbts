from typing import List


class Solution:
    # https://leetcode.com/problems/merge-intervals/
    def merge(self, intervals: List[List[int]]):
        res = []
        intervals_sorted = sorted(intervals, key=lambda x: x[0])

        for interval in intervals_sorted:
            start, end = interval
            if not len(res):
                res.append([start, end])
            else:
                prev_index = len(res) - 1
                prev_start, prev_end = res[prev_index]
                if start > prev_end:
                    res.append([start, end])
                else:
                    res[prev_index] = [prev_start, max(prev_end, end)]
        return res

    # https://leetcode.com/problems/interval-list-intersections/

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]):
        res = []

        ia, ib = 0, 0
        while ia < len(A) and ib < len(B):
            start_a, end_a = A[ia]
            start_b, end_b = B[ib]

            if start_a <= start_b and end_a >= start_b:
                start, end = start_b, min(end_a, end_b)
                res.append([start, end])
            elif start_b <= start_a and end_b >= start_a:
                start, end = start_a, min(end_a, end_b)
                res.append([start, end])

            if end_a < end_b:
                ia += 1
            else:
                ib += 1

        return res


s = Solution()
print(s.intervalIntersection([[0, 2], [5, 10], [13, 23], [
      24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
print(s.intervalIntersection([[4, 11]],
                             [[1, 2], [8, 11], [12, 13], [14, 15], [17, 19]]))
#  [[8,11]]
