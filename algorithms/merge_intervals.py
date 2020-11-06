from typing import List


class Solution:
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
