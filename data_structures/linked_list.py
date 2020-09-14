class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(val)
        current.next = new_node

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        current = self.head
        count = 0

        new_node = Node(val)

        if index == 0:
            self.head = new_node
        else:
            while current:
                if count == index - 1:
                    new_node.next = current.next
                    current.next = new_node
                count += 1
                current = current.next

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current = self.head
        count = 0

        if index == 0 and self.head:
            self.head = self.head.next
        else:
            while current:
                if count == index - 1:
                    current.next = current.next.next if current.next \
                        and current.next.next else None
                count += 1
                current = current.next


def main():
    print('## case 1\n')
    linkedList = MyLinkedList()    # Initialize empty LinkedList
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)    # linked list becomes 1 -> 2 -> 3
    print(linkedList.get(1))  # returns 2
    linkedList.deleteAtIndex(1)    # now the linked list is 1 -> 3
    print(linkedList.get(1))   # returns 3

    print('## case 2\n')
    linkedList = MyLinkedList()
    linkedList.addAtHead(7)  # 7
    linkedList.addAtTail(7)  # 7 -> 7
    linkedList.addAtHead(9)  # 9 -> 7 -> 7
    linkedList.addAtTail(8)  # 9 -> 7 -> 7 -> 8
    linkedList.addAtHead(6)  # 6 -> 9 -> 7 -> 7 -> 8
    linkedList.addAtHead(0)  # 0 -> 6 -> 9 -> 7 -> 7 -> 8
    print(linkedList.get(5))  # 8
    linkedList.addAtHead(0)  # 0 -> 0 -> 6 -> 9 -> 7 -> 7 -> 8
    print(linkedList.get(2))  # 6
    print(linkedList.get(5))  # 7
    linkedList.addAtTail(4)  # 0 -> 0 -> 6 -> 9 -> 7 -> 7 -> 8 -> 4

    print('## case 3\n')
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)  # 1
    linkedList.addAtTail(3)  # 1 -> 3
    linkedList.addAtIndex(1, 2)  # 1 -> 2 -> 3
    print(linkedList.get(1))  # 2
    linkedList.deleteAtIndex(0)  # 2 -> 3
    print(linkedList.get(0))  # 2

    print('## case 4\n')
    linkedList = MyLinkedList()
    linkedList.addAtIndex(0, 10)  # 10
    linkedList.addAtIndex(0, 20)  # 20 -> 10
    linkedList.addAtIndex(1, 30)  # 20 -> 30 -> 10
    print(linkedList.get(0))  # 20

    print('## case 5\n')
    linkedList = MyLinkedList()
    linkedList.addAtHead(2)  # 2
    linkedList.deleteAtIndex(1)  # nothing
    linkedList.addAtHead(2)  # 2 -> 2
    linkedList.addAtHead(7)  # 7 -> 2 -> 2
    linkedList.addAtHead(3)  # 3 -> 7 -> 2 -> 2
    linkedList.addAtHead(2)  # 2 -> 3 -> 7 -> 2 -> 2
    linkedList.addAtHead(5)  # 5 -> 2 -> 3 -> 7 -> 2 -> 2
    linkedList.addAtTail(5)  # 5 -> 2 -> 3 -> 7 -> 2 -> 2 -> 5
    print(linkedList.get(5))  # 2
    linkedList.deleteAtIndex(6)  # 5 -> 2 -> 3 -> 7 -> 2 -> 2
    linkedList.deleteAtIndex(4)  # 5 -> 2 -> 3 -> 7 -> 2


main()
