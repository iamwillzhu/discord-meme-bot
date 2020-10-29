import unittest

from models.date import Date


class TestDateComparisons(unittest.TestCase):

    def test_eq(self):
        date_one = Date(day=1, month=2, year=2010)
        date_two = Date(day=1, month=3, year=2010)

        self.assertEqual(date_one, date_one)
        self.assertNotEqual(date_one, date_two)

    def test_gt(self):
        date_one = Date(day=1, month=2, year=2010)
        date_two = Date(day=1, month=3, year=2010)

        self.assertGreater(date_two, date_one)

    def test_lt(self):
        date_one = Date(day=1, month=2, year=2010)
        date_two = Date(day=1, month=3, year=2010)

        self.assertLess(date_one, date_two)

    def test_le(self):
        date_one = Date(day=1, month=2, year=2010)
        date_two = Date(day=1, month=3, year=2010)

        self.assertLessEqual(date_one, date_one)
        self.assertLessEqual(date_one, date_two)

    def test_ge(self):
        date_one = Date(day=1, month=2, year=2010)
        date_two = Date(day=1, month=3, year=2010)

        self.assertGreaterEqual(date_two, date_two)
        self.assertGreaterEqual(date_two, date_one)

    def test_str(self):
        date = Date(day=1, month=2, year=2010)
        date_str = "02/01/2010"

        self.assertEqual(str(date), date_str)


if __name__ == "__main__":
    unittest.main()
