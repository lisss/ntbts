from algorithms.search_rotated_array import Solution


def test_search_rotated_array():
    s = Solution()

    assert s.search([2, 3, 1], 1) == 2
    assert s.search([3, 4, 5, 6, 7, 8, 1, 2], 1) == 6
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([1], 1) == 0
    assert s.search([3, 5, 1], 3) == 0
    assert s.search([5, 1, 3], 5) == 0
    assert s.search([5, 1, 3], 3) == 2
    assert s.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
    assert s.search([6, 7, 1, 2, 3, 4, 5], 6) == 0
