from unittest.mock import Mock
from datetime import datetime
import requests
from requests.exceptions import ConnectionError
import unittest


tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)


datetime = Mock()


def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()

    return 0 <= day_of_the_week < 5


datetime.today.return_value = saturday
assert not is_weekday()


requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestGetHolidays(unittest.TestCase):
    def test_get_holidays_connection(self):
        requests.get.side_effect = ConnectionError


if __name__ == '__main__':
    print(get_holidays())