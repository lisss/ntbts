import random

BUFF = 256


class RandomizedSet:
    def __init__(self):
        self.elems = [None] * BUFF
        self.nums_map = {}
        self.next_ind = 0

    def insert(self, val: int):
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        if val in self.nums_map:
            return False
        self.nums_map[val] = self.next_ind
        if self.next_ind == len(self.elems) - 1:
            self.elems.extend([None] * BUFF)
        self.elems[self.next_ind] = val
        self.next_ind += 1
        return True

    def remove(self, val: int):
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.nums_map:
            return False
        ind = self.nums_map[val]
        del self.nums_map[val]
        if not len(self.nums_map):
            self.elems[0] = None
            self.next_ind = 0
        else:
            self.nums_map[self.elems[self.next_ind - 1]] = ind
            self.elems[ind] = self.elems[self.next_ind - 1]
            self.elems[self.next_ind - 1] = None
            self.next_ind -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        if not len(self.nums_map):
            return -1
        if len(self.nums_map) == 1:
            return self.elems[0]
        rand = random.randint(0, self.next_ind - 1)
        val = self.elems[rand]
        return val
