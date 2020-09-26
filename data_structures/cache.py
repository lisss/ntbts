class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        self.lru = {}
        self.last_use = 0

    def get(self, key: int):
        if self.cache.get(key):
            item = self.cache[key]
            self.lru[self.last_use] = key
            del self.lru[item['last_use']]
            item['last_use'] = self.last_use
            self.last_use += 1
            return item['val']
        return -1

    def put(self, key: int, value: int):
        if self.cache.get(key):
            item = self.cache[key]
            self.cache[key] = {'val': value, 'last_use': self.last_use}
            self.lru[self.last_use] = key
            del self.lru[item['last_use']]
            self.last_use += 1
        else:
            if self.count == self.capacity:
                lru = min(self.lru.keys())
                del self.cache[self.lru[lru]]
                del self.lru[lru]
                self.count -= 1
            self.cache[key] = {'val': value, 'last_use': self.last_use}
            self.count += 1
            self.lru[self.last_use] = key
            self.last_use += 1
