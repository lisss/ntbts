class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head: Node):
    curr = head
    prev = None
    while curr:
        tmp_next = curr.next
        curr.next = prev
        prev = curr
        curr = tmp_next
    return prev


def reverse_sub_list(head: Node, p: int, q: int):
    if p == q:
        return head

    curr, prev = head, None
    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    last_node_first_part = prev
    last_node_sublist = curr
    temp_next = None

    i = 0
    while curr and i < q - p + 1:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
        i += 1

    if last_node_first_part:
        last_node_first_part.next = prev
    else:
        head = prev

    last_node_sublist.next = curr

    return head


def reverse_every_k_elements(head: Node, k: int):
    if k <= 1 or not head:
        return head

    curr, prev = head, None

    while curr:
        latest_prev_part = prev
        last_node_sub_list = curr
        i = 0

        while curr and i < k:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            i += 1

        if latest_prev_part:
            latest_prev_part.next = prev
        else:
            head = prev

        last_node_sub_list.next = curr
        prev = last_node_sub_list

    return head


def reverse_alternate_k_elements(head: Node, k: int):
    if k <= 1 or not head:
        return head

    curr, prev = head, None
    i = 0

    while curr:
        latest_prev_part = prev
        last_node_sub_list = curr

        while curr and i < k:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            i += 1

        if latest_prev_part:
            latest_prev_part.next = prev
        else:
            head = prev

        last_node_sub_list.next = curr

        while curr and i:
            prev = curr
            curr = curr.next
            i -= 1

    return head


def rotate(head, rotations):
    if not head or not head.next or rotations <= 0:
        return head

    l_len = 1
    curr, prev = head, None

    while curr:
        curr = curr.next
        l_len += 1

    curr, last_head = head, head
    start = rotations % l_len

    i = 0
    while curr and i < start:
        prev = curr
        curr = curr.next
        i += 1

    head = curr
    prev.next = None

    while curr.next:
        curr = curr.next

    curr.next = last_head

    return head


# solution provided in the course
def rotate_2(head, rotations):
    if head is None or head.next is None or rotations <= 0:
        return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    last_node.next = head  # connect the last node with the head to make it a circular list
    rotations %= list_length  # no need to do rotations more than the length of the list
    skip_length = list_length - rotations
    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = rotate(head, 8)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()
