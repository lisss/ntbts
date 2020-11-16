class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def calculate_cycle_len(slow):
    current = slow
    c_len = 0

    while True:
        current = current.next
        c_len += 1
        if current == slow:
            break
    return c_len


def find_start(head, c_len):
    p1, p2 = head, head

    while c_len:
        p2 = p2.next
        c_len -= 1

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def find_cycle_start(head):
    fast, slow = head, head
    c_len = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            c_len = calculate_cycle_len(slow)
            break
    return find_start(head, c_len)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
