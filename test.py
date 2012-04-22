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
        self.passengers = [User("Pablo", "pablo@pablo.com")]

class JourneyStopForBoardingTests(JourneyStopTests):
    def test_init(self):
        stop_for_boarding = JourneyStopForBoarding(self.where, self.when, self.passengers)

        self.assertEqual(self.where, stop_for_boarding.place)
        self.assertEqual(self.when, stop_for_boarding.datetime)
        self.assertEqual(self.passengers, stop_for_boarding.passengers)

class JourneyStopForDischargingTests(JourneyStopTests):
    def test_init(self):
        stop_for_discharging = JourneyStopForDischarging(self.where, self.when, self.passengers)

        self.assertEqual(self.where, stop_for_discharging.place)
        self.assertEqual(self.when, stop_for_discharging.datetime)
        self.assertEqual(self.passengers, stop_for_discharging.passengers)

class CommuterRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Pablo", "pablo@pablo.com")


    def test_register_a_request_for_commuting(self):
        """
        Como oficinista quiero registrar que
            todos los Lunes, Martes y Miercoles, salgo de mi casa a las 8:00 AM y tengo que llegar a mi trabajo a las 9:00 AM
            y los Jueves y Viernes salgo de la casa de mi novia a las 8:30 AM y tengo que llegar a mi trabajo a las 9:30 AM
        """
        pass

    def test_register_a_request_for_commuting_with_a_car_offer(self):
        """
        Como vendedor de autopartes quiero registrar que
            todos los Lunes, Miercoles y Viernes salgo de mi casa a las 7:00 AM y tengo que llegar a mi oficina en el centro a las 9:00 AM
            y los Martes y Jueves salgo de casa a las 8:00 AM y tengo que llegar al taller en Chararita a las 10:00 AM
            y quiero aclarar que los Miercoles dispongo de un auto con 4 asientos extra
        """
        pass


if __name__ == "__main__":
    unittest.main()
