# TODO: check linear probing
# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/

"""
Open hashing
"""

NUM_BUCKETS = 256


class Key:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.buckets = [None] * NUM_BUCKETS

    def __hash__(self, key):
        if type(key) == int:
            return key
        if type(key) == str:
            res = 0
            for i, x in enumerate(key):
                res += ord(x) * 10 + i + 1
            return res
        raise TypeError(f'Unhashable type #{type(key).__name__}')

    def put(self, key, value):
        index = self.__hash__(key) % NUM_BUCKETS

        if not self.buckets[index]:
            self.buckets[index] = Key(key, value)
        else:
            if self.buckets[index].key == key:
                self.buckets[index].value = value
            else:
                current = self.buckets[index]
                while current.next:
                    if current.key == key:
                        current.value = value
                        break
                    current = current.next
                if current.key == key:
                    current.value = value
                else:
                    current.next = Key(key, value)

    def get(self, key):
        index = self.__hash__(key) % NUM_BUCKETS

        if not self.buckets[index]:
            return -1

        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return -1

    def remove(self, key):
        index = self.__hash__(key) % NUM_BUCKETS

        if not self.buckets[index]:
            return

        if self.buckets[index].key == key and not self.buckets[index].next:
            self.buckets[index] = None
            return

        current = self.buckets[index]
        if self.buckets[index].key == key:
            self.buckets[index] = self.buckets[index].next
            current = current.next
        while current:
            if current.next and current.next.key == key:
                current.next = current.next.next
                break
            current = current.next


# tests assume NUM_BUCKETS = 3

print('\n--- case 1---')
hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.put(3, 5)
hashMap.put(4, 9)
hashMap.put(5, 99)
hashMap.put(6, 33)
hashMap.put(7, 22)
hashMap.put(8, 45)
print(hashMap.get(1))   # 1
print(hashMap.get(3))   # 5
print(hashMap.get(4))   # 9
print(hashMap.get(55))   # -1
hashMap.put(2, 1)
print(hashMap.get(2))   # 1
hashMap.put(7, 23)
print(hashMap.get(7))   # 23
hashMap.remove(4)
print(hashMap.get(4))   # -1
hashMap.put(77, 1)
hashMap.remove(26)
print(hashMap.get(77))  # 1
hashMap.put(501, 521)
hashMap.put(507, 58)
hashMap.put(504, 155)
hashMap.put(570, 521)
hashMap.remove(504)
print(hashMap.get(504))  # -1

print('\n--- case 2 ---')
hashMap = MyHashMap()
hashMap.put(504, 155)
hashMap.put(570, 521)
hashMap.remove(504)
print(hashMap.get(504))  # -1
