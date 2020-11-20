FULL_DEGREE = 360
HALF_DEGREE = FULL_DEGREE / 2
MIN_DEGREE = FULL_DEGREE / 60
HR_DEGREE = FULL_DEGREE / 12
HR_MIN_DEGREE = HR_DEGREE / 60
HR_START = 12


class Solution:
    def angleClock(self, hour: int, minutes: int):
        hr_diff = hour * HR_DEGREE if hour != HR_START else 0
        hr_min_diff = minutes * HR_MIN_DEGREE
        min_diff = minutes * MIN_DEGREE

        angle = abs(min_diff - (hr_diff + hr_min_diff))
        return angle if angle <= HALF_DEGREE else FULL_DEGREE - angle
