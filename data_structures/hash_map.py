class MyHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int):
        """
        value will always be non-negative.
        """
        self.map[key] = value

    def get(self, key: int):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        return self.map.get(key, -1)

    def remove(self, key: int):
        """
        Removes the mapping of the specified value key
        f this map contains a mapping for the key
        """
        if self.map.get(key):
            del self.map[key]
