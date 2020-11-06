from data_structures.merge_intervals import Solution


def test_merge_intervals():
    sb = Solution()
    assert sb.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sb.merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    assert sb.merge([[4, 4]]) == [[4, 4]]
    assert sb.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert sb.merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert sb.merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert sb.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert sb.merge([[2, 3], [4, 5], [1, 6]]) == [[1, 6]]
    assert sb.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
    assert sb.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
    assert sb.merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
