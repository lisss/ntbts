class DLNode:
    def __init__(self, key, data):
        self.prev = None
        self.next = None
        self.key = key
        self.data = data


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, node):
        new_node = node
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        if not self.tail:
            self.tail = self.head
        self.head = new_node

    def remove_tail(self):
        if not self.head:
            return
        if not self.tail:
            key = self.head.key
            self.head = None
            return key
        else:
            key = self.tail.key
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return key

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return -1


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.dllist = DLList()
        self.capacity = capacity

    def get(self, key):
        if not self.cache.get(key):
            return -1
        node = self.cache[key]
        if not node == self.dllist.head:
            if self.dllist.tail == node:
                self.dllist.tail = node.prev
            prev = node.prev
            next = node.next
            if next:
                next.prev = prev
            prev.next = next
            node.next = self.dllist.head
            self.dllist.add_head(node)

        return node.data

    def put(self, key, value):
        if self.cache.get(key):
            item = self.cache[key]
            item.data = value
            self.dllist.add_head(item)
            if len(self.cache) == self.capacity:
                self.dllist.remove_tail()
        else:
            node = DLNode(key, value)
            if len(self.cache) == self.capacity:
                key_del = self.dllist.remove_tail()
                del self.cache[key_del]
            self.dllist.add_head(node)
            self.cache[key] = node
