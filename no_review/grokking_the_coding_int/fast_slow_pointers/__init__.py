from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def _reverse(head):
    prev = None
    while head:
        tmp_next = head.next
        head.next = prev
        prev = head
        head = tmp_next
    return prev


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


def is_list_palindrome(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    head_snd = _reverse(slow)
    copy_head_snd = head_snd

    while head and head_snd:
        if head.value != head_snd.value:
            return False
        head = head.next
        head_snd = head_snd.next

    _reverse(copy_head_snd)

    if not head or not head_snd:
        return True

    return False


def reorder(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    snd_head = _reverse(slow)
    curr = head

    while curr and snd_head:
        tmp_next = curr.next
        curr.next = snd_head
        curr = tmp_next

        tmp_next = snd_head.next
        snd_head.next = curr
        snd_head = tmp_next

    if curr:
        curr.next = None


def circular_array_loop_exists(arr: List[int]):
    def _find_next_index(is_forward, curr_index):
        direction = arr[curr_index] >= 0

        # different directions
        if direction != is_forward:
            return -1

        next_index = (curr_index + arr[curr_index]) % len(arr)

        # single element loop
        if next_index == curr_index:
            return -1

        return next_index

    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        fast, slow = i, i

        while True:
            slow = _find_next_index(is_forward, slow)
            fast = _find_next_index(is_forward, fast)

            if fast != -1:
                fast = _find_next_index(is_forward, fast)

            if fast == -1 or slow == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True

    return False
