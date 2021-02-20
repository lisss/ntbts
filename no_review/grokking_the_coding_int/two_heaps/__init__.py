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


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(capital)):
        heappush(min_capital_heap, (capital[i], i))
    return


find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)
