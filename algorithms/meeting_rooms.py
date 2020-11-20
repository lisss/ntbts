
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
