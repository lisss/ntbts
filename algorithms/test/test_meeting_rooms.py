from algorithms.meeting_rooms import Solution


def test_meeting_rooms():
    s = Solution()

    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[4, 5], [3, 6], [2, 5]]) == 3
    assert s.minMeetingRooms([[13, 15], [1, 13]]) == 1
    assert s.minMeetingRooms([[1, 5], [8, 9], [8, 9]]) == 2
