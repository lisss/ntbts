
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals = sorted(intervals, key=lambda x: x[0])
        booked_clots = []

        for start, end in intervals:
            if not len(booked_clots):
                heapq.heappush(booked_clots, end)
            else:
                last_end = heapq.nsmallest(1, booked_clots)[0]
                if start >= last_end:
                    heapq.heappop(booked_clots)
                heapq.heappush(booked_clots, end)

        return len(booked_clots)

    def kClosest(self, points: List[List[int]], K: int):
        def _get_dist(p):
            return p[0] ** 2 + p[1] ** 2

        res = []
        final_res = []

        for x in points:
            heapq.heappush(res, (_get_dist(x), x))

        for _ in range(K):
            _, x = heapq.heappop(res)
            final_res.append(x)

        return final_res
