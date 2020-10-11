from data_structures.add_binary import Solution


def test_add_binary():
    sb = Solution()
    assert sb.addBinary('11', '1') == '100'
    assert sb.addBinary('1010', '1011') == '10101'
    assert sb.addBinary('0', '0') == '0'
    assert sb.addBinary('1111', '1111') == '11110'
    assert sb.addBinary('100', '110010') == '110110'
