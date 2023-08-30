import unittest
from parameterized import parameterized
from src.functions import *


class TestFunctions(unittest.TestCase):
    @parameterized.expand([
        ["2020-10-01", True],
        ["2022-09-07", True],
        ["2022-20-20", False],
        ["2019-09-30", True],
        ["2019-09-31", False],
        ["202-09-07", False],
        ["10-09-2025", False],
        ["20-2009-07", False],
    ])
    def test_valid_dates(self, date_to_test, expected):
        """
        Test valid dates
        """
        today = datetime.strptime("2023-08-30", "%Y-%m-%d").date()
        result = check_date(today, date_to_test)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["2019-01-01", 92],
        ["2021-02-01", 123],
        ["2022-09-30", 364],
        ["2022-10-01", 0],
        ["2022-10-02", 1],
        ["2022-11-02", 32]
    ])
    def test_days_to_birthday(self, birth_date, expected_days):
        """
        Test days to birthday
        """
        today = datetime.strptime("2022-10-01", "%Y-%m-%d").date()
        date_to_test = datetime.strptime(birth_date, "%Y-%m-%d").date()
        result = days_to_birthday(today, date_to_test)
        self.assertEqual(result, expected_days)

if __name__ == '__main__':
    unittest.main()