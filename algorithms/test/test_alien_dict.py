from algorithms.alien_dict import Solution


def test_alient_dict():
    s = Solution()

    assert s.isAlienSorted(['', ''],
                           'hlabcdefgijkmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['hello', 'leetcode'],
                           'hlabcdefgijkmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['word', 'world', 'row'],
                           'worldabcefghijkmnpqstuvxyz') is False
    assert s.isAlienSorted(
        ['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') is False
    assert s.isAlienSorted(['app', 'app', 'apple'],
                           'abcdefghijklmnopqrstuvwxyz') is True
    assert s.isAlienSorted(['app', 'app', 'ab'],
                           'abcdefghijklmnopqrstuvwxyz') is False
