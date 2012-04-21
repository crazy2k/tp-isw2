import unittest

from datetime import datetime

from tp import *

class UserTests(unittest.TestCase):
    def test_init(self):
        user = User("Pablo", "pablo@pablo.com")

        self.assertEqual("Pablo", user.name)
        self.assertEqual("pablo@pablo.com", user.email)

class DayOfWeekTests(unittest.TestCase):
    def test_init(self):
        lunes = DayOfWeek("Lunes", 0)

        self.assertEqual("Lunes", lunes.name)
        self.assertEqual(0, lunes.ordinal)

    def test_lt(self):
        lunes = DayOfWeek("Lunes", 0)
        martes = DayOfWeek("Martes", 1)

        self.assertTrue(lunes < martes)

class JourneyStopTests(unittest.TestCase):
    def setUp(self):
        self.where = Place()
        self.when = datetime.now
        self.passenger = User("Pablo", "pablo@pablo.com")

class JourneyStopForBoardingTests(JourneyStopTests):
    def test_init(self):
        stop_for_boarding = JourneyStopForBoarding(self.where, self.when, self.passenger)

        self.assertEqual(self.where, stop_for_boarding.place)
        self.assertEqual(self.when, stop_for_boarding.datetime)
        self.assertEqual(self.passenger, stop_for_boarding.passenger)

class JourneyStopForDischargingTests(JourneyStopTests):
    def test_init(self):
        stop_for_discharging = JourneyStopForDischarging(self.where, self.when, self.passenger)

        self.assertEqual(self.where, stop_for_discharging.place)
        self.assertEqual(self.when, stop_for_discharging.datetime)
        self.assertEqual(self.passenger, stop_for_discharging.passenger)


if __name__ == "__main__":
    unittest.main()
