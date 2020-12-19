
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

    # https://leetcode.com/problems/k-closest-points-to-origin/
    # TODO: try to sort heapq desc
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

    # https://leetcode.com/problems/task-scheduler/
    def leastInterval(self, tasks: List[str], n: int):
        freq_map = {}
        heap_list = []
        freq_max = 0
        idle = 0

        for t in tasks:
            if t not in freq_map:
                freq_map[t] = 0
            freq_map[t] += 1

        for t in freq_map:
            heapq.heappush(heap_list, (-freq_map[t], t))

        while heap_list:
            freq, _ = heapq.heappop(heap_list)
            freq = -freq
            if not freq_max:
                freq_max = freq
                idle = (freq - 1) * n
            else:
                idle -= min(freq_max - 1, freq)

        idle = max(idle, 0)
        return len(tasks) + idle
