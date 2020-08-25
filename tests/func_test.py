import unittest
import datetime


class TestFunc(unittest.TestCase):
    def test_date(self):
        dts = '2020-08-20'

        dt = datetime.datetime.strptime(dts, "%Y-%m-%d").date()

        yestoday = dt + datetime.timedelta(days=-1)
        print(type(yestoday))

        # expect = datetime.datetime(2020, 8, 20)

        self.assertEqual(str(yestoday), '2020-08-19')


if __name__ == "__main__":
    unittest.main()
