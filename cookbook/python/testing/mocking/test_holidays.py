# https://realpython.com/python-mock-library/

import unittest
from unittest.mock import patch

import requests
from holidays import get_holidays
from requests.exceptions import Timeout


class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch("holidays.requests") as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

class TestHolidays2(unittest.TestCase):
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

if __name__ == "__main__":
    unittest.main()
