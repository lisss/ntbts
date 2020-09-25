class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dequeue = [None] * k
        self.start = 0
        self.end = 0

    def insertFront(self, value: int):
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.dequeue[self.start] = value
            return True
        self.start = (self.start - 1) % len(self.dequeue)
        self.dequeue[self.start] = value
        return True

    def insertLast(self, value: int):
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.dequeue[self.end] = value
            return True
        self.end = (self.end + 1) % len(self.dequeue)
        self.dequeue[self.end] = value
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.dequeue[self.start] = None
        # it was the last element, so the queue is empty now,
        # resetting indicies
        if self.start == self.end:
            self.start = 0
            self.end = 0
        elif self.start == len(self.dequeue) - 1:
            self.start = 0
        elif not self.isEmpty():
            self.start += 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.dequeue[self.end] = None
        # it was the last element, so the queue is empty now,
        # resetting indicies
        if self.start == self.end:
            self.start = 0
            self.end = 0
        elif self.end:
            self.end -= 1
        elif not self.isEmpty():
            self.end = len(self.dequeue) - 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dequeue[self.start]

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dequeue[self.end]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.start == self.end and not self.dequeue[self.start]

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        if self.start:
            return self.start - self.end == 1
        else:
            return self.end == len(self.dequeue) - 1


print('\n--- case 1 ---')
dequeue = MyCircularDeque(3)
print(dequeue.insertLast(1))		# return true
print(dequeue.insertLast(2)	)		# return true
print(dequeue.insertFront(3))		# return true
print(dequeue.insertFront(4))		# return false
print(dequeue.getRear()) 			# return 2
print(dequeue.isFull())				# return true
print(dequeue.deleteLast())			# return true
print(dequeue.insertFront(4))		# return true
print(dequeue.getFront())			# return 4

print('\n--- case 2 ---')
dequeue = MyCircularDeque(5)
print(dequeue.insertFront(9))       # return true
print(dequeue.insertLast(1))		# return true
print(dequeue.insertLast(2))		# return true
print(dequeue.insertFront(3))		# return true
print(dequeue.insertFront(4))		# return true
print(dequeue.insertFront(5))		# return false
print(dequeue.insertFront(6))		# return false
print(dequeue.getRear())  			# return 2
print(dequeue.isFull())				# return true
print(dequeue.deleteLast())			# return true
print(dequeue.insertFront(4))		# return true
print(dequeue.getFront())			# return 4

print('\n--- case 3 ---')
dequeue = MyCircularDeque(2)
print(dequeue.insertFront(3))       # return true
print(dequeue.getRear())            # 3
print(dequeue.getFront())           # 3
print(dequeue.insertFront(7))       # return true
print(dequeue.getRear())            # 3
print(dequeue.getFront())           # 7
print(dequeue.deleteFront())        # return true
print(dequeue.getRear())            # 3
print(dequeue.getFront())           # 3
print(dequeue.insertLast(2))		# return true
print(dequeue.getRear())            # 2
print(dequeue.getFront())           # 3

print('\n--- case 4 ---')
dequeue = MyCircularDeque(4)
print(dequeue.insertFront(9))       # true
print(dequeue.deleteLast())         # true
print(dequeue.getRear())            # -1
print(dequeue.getFront())           # -1
print(dequeue.getFront())           # -1
print(dequeue.deleteFront())        # false
print(dequeue.insertFront(6))       # true
print(dequeue.insertLast(5))        # true
print(dequeue.insertFront(9))       # true
print(dequeue.getFront())           # 9
print(dequeue.insertFront(6))       # true

print('\n--- case 5 ---')
dequeue = MyCircularDeque(2)
print(dequeue.insertFront(9))       # true
print(dequeue.insertFront(3))       # true
print(dequeue.deleteFront())        # true
print(dequeue.getFront())           # 9
print(dequeue.deleteFront())        # true
print(dequeue.getFront())           # -1
print(dequeue.deleteFront())        # false
print(dequeue.getFront())           # -1

print('\n--- case 6 ---')
dequeue = MyCircularDeque(77)
print(dequeue.insertFront(89))      # true
print(dequeue.getRear())            # 89
print(dequeue.deleteLast())         # true
print(dequeue.getRear())            # -1
print(dequeue.insertFront(19))      # true
print(dequeue.insertFront(23))      # true
print(dequeue.insertFront(23))      # true
print(dequeue.insertFront(82))      # true
print(dequeue.isFull())             # false
print(dequeue.insertFront(45))      # true
print(dequeue.isFull())             # false
print(dequeue.getRear())            # 19
print(dequeue.deleteLast())         # true
print(dequeue.getFront())           # 45
print(dequeue.getFront())           # 45
print(dequeue.insertLast(74))       # true

print('\n--- case 7 ---')
dequeue = MyCircularDeque(731)
print(dequeue.insertFront(344))     # true
print(dequeue.insertFront(433))     # true
print(dequeue.deleteFront())        # true
print(dequeue.insertLast(504))      # true
print(dequeue.deleteFront())        # true
print(dequeue.getFront())           # 504
print(dequeue.insertLast(317))      # true
print(dequeue.deleteLast())         # true
print(dequeue.insertLast(608))      # true
print(dequeue.getRear())            # 608
print(dequeue.getRear())            # 608
print(dequeue.getFront())           # 504


print('\n--- case 8 ---')
dequeue = MyCircularDeque(8)
print(dequeue.insertFront(5))       # true
print(dequeue.deleteFront())        # true
print(dequeue.insertLast(3))        # true
print(dequeue.getRear())            # 3
print(dequeue.insertLast(7))        # true
print(dequeue.insertFront(7))       # true


print('\n--- case 9 ---')
dequeue = MyCircularDeque(3)
print(dequeue.insertFront(5))       # true
print(dequeue.insertFront(332))     # true
print(dequeue.deleteLast())         # true
print(dequeue.deleteFront())        # true
print(dequeue.isEmpty())            # true
print(dequeue.getRear())            # -1
print(dequeue.getFront())           # -1


print('\n--- case 10 ---')
dequeue = MyCircularDeque(3)
print(dequeue.insertFront(93))      # true
print(dequeue.insertLast(578))      # true
print(dequeue.deleteFront())        # true
print(dequeue.deleteLast())         # true
print(dequeue.insertLast(533))      # true
