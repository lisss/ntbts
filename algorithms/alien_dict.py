from typing import List


class Solution:
    def __init__(self):
        self.order_dict = {}

    def _compare_2_words(self, w1: str, w2: str):
        l1 = len(w1)
        l2 = len(w2)
        end = 0
        while end < l1 and end < l2:
            ch1, ch2 = self.order_dict[w1[end]], self.order_dict[w2[end]]
            if ch1 < ch2:
                return True
            if ch1 > ch2:
                return False
            end += 1

        if end == l1:
            return True
        if end == l2:
            return False

        return False

    def isAlienSorted(self, words: List[str], order: str):
        i1, i2 = 0, 1

        for i, c in enumerate(order):
            self.order_dict[c] = i

        while i2 < len(words):
            if not self._compare_2_words(words[i1], words[i2]):
                return False
            i1 += 1
            i2 += 1

        return True
