from data_structures.randomized_set import RandomizedSet


def test_randomized_set_1():
    randomizedSet = RandomizedSet()

    assert randomizedSet.insert(1) is True
    assert randomizedSet.remove(2) is False
    assert randomizedSet.insert(2) is True
    assert randomizedSet.getRandom() in [1, 2]
    assert randomizedSet.remove(1) is True
    assert randomizedSet.insert(2) is False
    assert randomizedSet.getRandom() == 2


def test_randomized_set_2():
    randomizedSet = RandomizedSet()

    assert randomizedSet.remove(0) is False
    assert randomizedSet.insert(0) is True
    assert randomizedSet.getRandom() == 0
    assert randomizedSet.remove(0) is True
    assert randomizedSet.insert(0) is True
