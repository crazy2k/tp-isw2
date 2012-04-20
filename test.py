import unittest

from datetime import datetime

from tp import *

class UserTests(unittest.TestCase):
    def test_init(self):
        user = User("Pablo", "pablo@pablo.com")
        self.assertEqual("Pablo", user.name)
        self.assertEqual("pablo@pablo.com", user.email)

class JourneyStopTests(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.occurrence = SingleTimeOccurrence(datetime.now)
        self.passenger = User("Pablo", "pablo@pablo.com")

    def test_init(self):
        stop = JourneyStop(self.place, self.occurrence, self.passenger)
        self.assertEqual(self.place, stop.place)
        self.assertEqual(self.occurrence, stop.occurrence)
        self.assertEqual(self.passenger, stop.passenger)


if __name__ == "__main__":
    unittest.main()
