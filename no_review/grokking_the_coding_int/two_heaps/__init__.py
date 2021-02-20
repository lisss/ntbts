from heapq import *
import heapq
from typing import List


class MedianOfAStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0] / 1.0


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def rebalanse(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove(self, heap: List[int], elem: int):
        ind = heap.index(elem)  # find the element
        del heap[ind]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def find_sliding_window_median(self, nums: List[int], k: int):
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if not self.max_heap or -self.max_heap[0] >= num:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

            self.rebalanse()

            if i - k + 1 >= 0:
                if len(self.min_heap) == len(self.max_heap):
                    result.append((-self.max_heap[0] + self.min_heap[0]) / 2)
                else:
                    result.append(-self.max_heap[0] / 1.0)

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)

                self.rebalanse()

        return result


def find_maximum_capital(capital, profits, num_projects, initial_capital):
    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(capital)):
        heappush(min_capital_heap, (capital[i], i))

    available_capital = initial_capital
    for _ in range(num_projects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))

        if not max_profit_heap:
            break

        available_capital += -heappop(max_profit_heap)[0]

    return available_capital


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals: List[Interval]):
    result = [None] * len(intervals)
    heap_start = []
    heap_end = []

    for i in range(len(intervals)):
        heappush(heap_start, (-intervals[i].start, i))
        heappush(heap_end, (-intervals[i].end, i))

    for _ in intervals:
        top_end, end_idx = heappop(heap_end)
        result[end_idx] = -1

        if -heap_start[0][0] >= -top_end:
            top_start, start_idx = heappop(heap_start)

            while heap_start and -heap_start[0][0] >= -top_end:
                top_start, start_idx = heappop(heap_start)
            result[end_idx] = start_idx

            heappush(heap_start, (top_start, start_idx))

    return result
