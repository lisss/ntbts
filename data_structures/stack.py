from typing import List


class Stack:
    def __init__(self):
        self.arr = [None] * 4
        self.last = -1
        self.empty = True

    def push(self, val):
        self.last += 1
        self.empty = False
        self.arr[self.last] = val
        if self.last == len(self.arr) - 1:
            self.arr.extend([None] * len(self.arr))
        return self.arr

    def pop(self):
        self.arr[self.last] = None
        self.last -= 1
        if self.last < 0:
            self.empty = True
        return self.arr

    def is_empty(self):
        return self.empty


# https://leetcode.com/problems/exclusive-time-of-functions/
class CallStack:
    def __init__(self, n):
        self.n = n + 1
        self.arr = [0] * self.n
        self.last = -1

    def push(self, val):
        self.last += 1
        if self.last == len(self.arr) - 1:
            self.arr.extend([0] * self.n)
        self.arr[self.last] = val

    def pop(self):
        last = self.arr[self.last]
        self.last -= 1
        return last

    def is_empty(self):
        return self.last == -1

    def peek(self):
        return self.arr[self.last] if self.last >= 0 else 0


class CallStackSolution:
    def exclusiveTime(self, n: int, logs: List[str]):
        stack = CallStack(n)
        res = [0] * n
        prev = 0

        for log in logs:
            fn_id, event, time = log.split(':')
            time = int(time)
            fn_id = int(fn_id)

            last = stack.peek()

            if event == 'start':
                if not stack.is_empty():
                    res[last] += time - prev
                stack.push(fn_id)
                prev = time
            else:
                res[last] += time - prev + 1
                stack.pop()
                prev = time + 1

        return res


def main():
    stack = Stack()
    print(stack.push(1))
    print(stack.push(3))
    print(stack.push(7))
    print(stack.push(8))
    print(stack.push(9))
    print(stack.push(10))
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())

    stack = Stack()
    print(stack.push(1))
    print(stack.pop())
    print(stack.is_empty())

    stack = Stack()
    print(stack.is_empty())
    print(stack.pop())
    print(stack.push(2))
    print(stack.is_empty())
    print(stack.push(5))
    print(stack.push(8))
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())


main()
