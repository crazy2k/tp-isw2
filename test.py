import unittest

import datetime

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

class JourneyOrganizerTest(unittest.TestCase):

    def setUp(self):
        def proposal_with_car():
            proponent = User("Pablo", "pablo@pablo.com")
            address1 = Address()
            address2 = Address()
            timetable = WeeklyTimetable(datetime.time(8, 30), (MONDAY,)) 
            return JourneyProposalWithVehicule(proponent, address1, address2, 
                timetable, 2)

        def proposal_without_car():
            proponent = User("Rodrigo", "rodrigo@rodrigo.com")
            address1 = Address()
            address2 = Address()
            timetable = WeeklyTimetable(datetime.time(8, 25), (MONDAY,)) 
            return JourneyProposalWithoutVehicule(proponent, address1, address2, 
                timetable)

        self.proposal_with_car = proposal_with_car() 
        self.proposal_without_car = proposal_without_car() 
        self.timedelta = datetime.timedelta(minutes=15)
        self.aweek_interval = DateTimeInterval(datetime.datetime(2012, 5, 14), datetime.datetime(2012, 5, 19))
        self.distance_tolerance = 10

        self.organizer = JourneyOrganizer([self.proposal_with_car, self.proposal_without_car],
            self.aweek_interval, self.timedelta, self.distance_tolerance)


    def test_organizer_should_create_journey_for_compatible_proposals(self):
        journeys = self.organizer.organize()

        assertEqual(1, len(journeys))

        journey = journeys[0]
        assertEqual(self.proposal_with_car, journey.accepted_proposal)
        assertEqual(2, len(journeys.stops))

        stops = journeys.stops
        assertEqual(self.proposal_with_car.origin, stops[0].place)
        assertEqual(self.proposal_with_car.destination, stops[1].place)

        assertTrue(self.proposal_without_car.origin.is_near(stops[0].place, self.distance_tolerance))
        assertTrue(self.proposal_without_car.destination.in_near(stops[1].place, self.distance_tolerance))

        users = {self.proposal_with_car.proponent, self.proposal_without_car.proponent}
        assertEqual(users, set(self.stops[0].passengers_stepping_in))
        assertEqual(users, set(self.stops[1].passengers_leaving))
        assertEqual(0, len(self.stops[0].passengers_leaving))
        assertEqual(0, len(self.stops[1].passengers_stepping_in))

        delta = self.stops[0].datetime - self.proposal_without_car.timetable.ocurrences()[0]
        assertTrue(abs(delta.total_seconds()) <= self.timedelta.total_seconds())

        delta = self.stops[0].datetime - self.proposal_with_car.timetable.ocurrences()[0]
        assertTrue(abs(delta.total_seconds()) <= self.timedelta.total_seconds())

        assertEqual(journeys.stops[0].datetime.date(), journey.date())

        

if __name__ == "__main__":
    unittest.main()
