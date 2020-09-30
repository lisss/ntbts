import pytest
from mock import patch
from contextlib import contextmanager
from data_structures.rate_limiter import RateLimiter, RateExceededException


@contextmanager
def not_raises(exception):
    try:
        yield
    except exception:
        raise pytest.fail("DID RAISE {0}".format(exception))


@patch('time.sleep', return_value=None)
def test_1(patched_time_sleep):
    with not_raises(RateExceededException):
        print(patched_time_sleep)
        limiter = RateLimiter()
        print('1st call')
        patched_time_sleep(0.1)
        limiter.can_make_request()

        print('2nd call')
        patched_time_sleep(0.1)
        limiter.can_make_request()

        print('3rd call')
        patched_time_sleep(0.1)
        limiter.can_make_request()


@patch('time.sleep', return_value=None)
def test_2(patched_time_sleep):
    print(patched_time_sleep)
    with pytest.raises(RateExceededException):
        limiter = RateLimiter()
        print('1st call')
        patched_time_sleep(0.1)
        limiter.can_make_request()

        print('2nd call')
        patched_time_sleep(0.1)
        limiter.can_make_request()

        print('3rd call')
        patched_time_sleep(0.1)
        limiter.can_make_request()

        print('4th call')
        patched_time_sleep(0.1)
        limiter.can_make_request()
