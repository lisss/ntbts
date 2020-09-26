from data_structures.cache import LRUCache


def test_lru_1():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4


def test_lru_2():
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    assert lRUCache.get(2) == 1
    lRUCache.put(4, 1)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(2) == 1


def test_lru_3():
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(2) == 3


def test_lru_4():
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(3, 2)
    assert lRUCache.get(3) == 2
    assert lRUCache.get(2) == 1
    lRUCache.put(4, 3)
    assert lRUCache.get(2) == 1
    assert lRUCache.get(3) == -1
    assert lRUCache.get(4) == 3
