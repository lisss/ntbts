
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals = sorted(intervals, key=lambda x: x[0])
        booked_clots = []
        count = 0

        for start, end in intervals:
            if not len(booked_clots):
                heapq.heappush(booked_clots, (end, count))
                count += 1
            else:
                last_end, _ = heapq.nsmallest(1, booked_clots)[0]
                if start >= last_end:
                    heapq.heappop(booked_clots)
                heapq.heappush(booked_clots, (end, count))
                count += 1

        return len(booked_clots)
