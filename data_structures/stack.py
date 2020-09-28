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
