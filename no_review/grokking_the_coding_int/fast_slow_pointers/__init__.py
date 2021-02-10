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


def find_happy_number(num):
    def _find_sum(num):
        _sum = 0
        while (num > 0):
            digit = num % 10
            _sum += digit * digit
            num //= 10
        return _sum

    fast, slow = num, num

    while True:
        slow = _find_sum(slow)
        fast = _find_sum(_find_sum(fast))
        if slow == fast:
            break
    return slow == 1


def find_middle_of_linked_list(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
