from datetime import datetime


class RateExceededException(Exception):
    pass


class RateLimiter:
    def __init__(self):
        self.requests = []

    def can_make_request(self):
        curr_time = datetime.now()
        if len(self.requests) == 3:
            for x in self.requests:
                if curr_time.second - x.second > 60:
                    del x
            if len(self.requests) == 3:
                raise RateExceededException('soryan')
            else:
                self.requests.append(curr_time)
        else:
            self.requests.append(curr_time)
