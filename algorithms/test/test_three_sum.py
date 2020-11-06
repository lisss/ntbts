from algorithms.three_sum import Solution


def test_three_sum():
    s = Solution()
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([-1, 0, 1, 2, -1, -4, -1]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3],
                                                [-2, 0, 2], [-1, 0, 1]]
