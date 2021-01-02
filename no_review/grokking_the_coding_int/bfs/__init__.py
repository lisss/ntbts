from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next
        print()


# Binary Tree Level Order Traversal (easy)
def traverse(root: TreeNode):
    result = []
    if not root:
        return

    queue = deque()

    queue.append(root)

    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            curr_node = queue.popleft()
            curr_level.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
        result.append(curr_level)

    return result


def reverse_traverse(root: TreeNode):
    if not root:
        return

    queue = deque()
    result = deque()

    queue.append(root)

    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            curr_node = queue.popleft()
            curr_level.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
        result.appendleft(curr_level)

    return result


def zigzag_traverse(root: TreeNode):
    if not root:
        return

    result = []
    queue = deque()

    queue.append(root)

    while queue:
        level_size = len(queue)
        curr_level = deque()

        for _ in range(level_size):
            curr_node = queue.popleft()
            if not level_size % 2:
                curr_level.appendleft(curr_node.val)
            else:
                curr_level.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
        result.append(list(curr_level))

    return result


def find_level_averages(root: TreeNode):
    if not root:
        return 0
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        curr_level = []
        curr_level_sum = 0

        for _ in range(level_size):
            curr_node = queue.popleft()
            curr_level.append(curr_node.val)
            curr_level_sum += curr_node.val

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
        result.append(curr_level_sum / level_size)

    return result


def find_minimum_depth(root: TreeNode):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    min_depth = 0

    while queue:
        min_depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            curr_node = queue.popleft()
            if not curr_node.left and not curr_node.right:
                return min_depth

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
    return 0


def find_successor(root: TreeNode, key: int):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            curr_node = queue.popleft()

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            if curr_node.val == key:
                return queue.popleft() if queue else None
    return


# Connect Level Order Siblings (medium)
def connect_level_order_siblings(root: TreeNode):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        prev_node = None
        for _ in range(level_size):
            curr_node = queue.popleft()
            if prev_node:
                prev_node.next = curr_node
            prev_node = curr_node
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)


def connect_all_siblings(root: TreeNode):
    if not root:
        return

    queue = deque()
    queue.append(root)

    prev_node = root
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            curr_node = queue.popleft()
            prev_node.next = curr_node
            prev_node = curr_node
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)


def tree_right_view(root: TreeNode):
    if not root:
        return
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            if i == level_size - 1:
                result.append(curr_node)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)
result = tree_right_view(root)
print("Tree right view: ")
for node in result:
    print(str(node.val) + " ", end='')
print()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = tree_right_view(root)
print("Tree right view: ")
for node in result:
    print(str(node.val) + " ", end='')
print()
