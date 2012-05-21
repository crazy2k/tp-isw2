import unittest

from tp import *

class UserTests(unittest.TestCase):
    def test_init(self):
        user = User("Pablo", "pablo@pablo.com")

        self.assertEqual("Pablo", user.name)
        self.assertEqual("pablo@pablo.com", user.email)

class DayOfWeekTests(unittest.TestCase):
    def test_init(self):
        lunes = DayOfWeek("Lunes")

        self.assertEqual("Lunes", lunes.name)

    def test_lt(self):
        self.assertTrue(MONDAY < TUESDAY)

class JourneyStopTests():
    def setUp(self):
        self.where = Place()
        self.passengers = [User("Pablo", "pablo@pablo.com")]

    def test_init(self):
        stop = JourneyStop(self.where, self.passengers, [])

        self.assertEqual(self.where, stop.place)
        self.assertEqual(self.passengers, stop.passengers_stepping_in)
        self.assertEqual([], stop.passengers_leaving)

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Pablo", "pablo@pablo.com")


    def test_register_a_journey_proposal(self):
        """
        Como oficinista quiero registrar que
        todos los Lunes, Martes y Miercoles, salgo de mi casa a las 8:00 AM y tengo que llegar a mi trabajo a las 9:00 AM
        y los Jueves y Viernes salgo de la casa de mi novia a las 8:30 AM y tengo que llegar a mi trabajo a las 9:30 AM
    """
    pass

    def test_register_a_journey_proposal_with_a_car_offer(self):
        """
        Como vendedor de autopartes quiero registrar que
            todos los Lunes, Miercoles y Viernes salgo de mi casa a las 7:00 AM y tengo que llegar a mi oficina en el centro a las 9:00 AM
            y los Martes y Jueves salgo de casa a las 8:00 AM y tengo que llegar al taller en Chararita a las 10:00 AM
            y quiero aclarar que los Miercoles dispongo de un auto con 4 asientos extra
        """
        pass

class SimpleJourneyOrganizerTest(unittest.TestCase):
    def setUp(self):
        def proposal_with_car():
            proponent = User("Pablo", "pablo@pablo.com")
            address1 = Address()
            address2 = Address()
            timetable = WeeklyTimetable(time(8, 30), (MONDAY,))
            return JourneyProposalWithVehicule(proponent, address1, address2, 
                timetable, 2)

        def proposal_without_car():
            proponent = User("Rodrigo", "rodrigo@rodrigo.com")
            address1 = Address()
            address2 = Address()
            timetable = WeeklyTimetable(time(8, 25), (MONDAY,))
            return JourneyProposalWithoutVehicule(proponent, address1, address2, 
                timetable)

        self.proposal_with_car = proposal_with_car() 
        self.proposal_without_car = proposal_without_car() 
        self.timedelta = timedelta(minutes=15)
        self.week_interval = DateTimeInterval(datetime(2012, 5, 14), datetime(2012, 5, 19))
        self.distance_tolerance = 10

        self.organizer = SimpleJourneyOrganizer([self.proposal_with_car, self.proposal_without_car],
            self.week_interval, self.timedelta, self.distance_tolerance)


    def test_organizer_should_create_journey_for_compatible_proposals(self):
        journey_schedule = self.organizer.organize()

        self.assertEqual(1, journey_schedule.total_journeys())

        journey = journey_schedule.journeys_for(self.proposal_with_car.proponent)[0]
        self.assertEqual(self.proposal_with_car, journey.accepted_proposal)
        self.assertEqual(2, len(journey.stops))

        stops = journey.stops
        self.assertEqual(self.proposal_with_car.origin, stops[0].place)
        self.assertEqual(self.proposal_with_car.destination, stops[1].place)

        self.assertTrue(self.proposal_without_car.origin.is_near(stops[0].place, self.distance_tolerance))
        self.assertTrue(self.proposal_without_car.destination.is_near(stops[1].place, self.distance_tolerance))

        users = {self.proposal_with_car.proponent, self.proposal_without_car.proponent}
        self.assertEqual(users, set(stops[0].passengers_stepping_in))
        self.assertEqual(users, set(stops[1].passengers_leaving))
        self.assertEqual(0, len(stops[0].passengers_leaving))
        self.assertEqual(0, len(stops[1].passengers_stepping_in))

        delta = journey.datetime - self.proposal_without_car.timetable.ocurrences_at(self.week_interval)[0]
        self.assertTrue(abs(delta.total_seconds()) <= self.timedelta.total_seconds())

        self.assertEqual(journey.datetime.date(), journey.date())

        
    def test_organizer_should_notify_when_a_proposal_was_not_posible_to_organize(self):
        journey_schedule = self.organizer_with_left_over_poposal.organize()

        self.assertEqual(1, journey_schedule.total_journeys())

        journey = journey_schedule.journeys_for_at(self.proposal_with_car.proponent, self.interval)

        self.assertEqual(self.proposal_with_car, journey.accepted_proposal)

        try:
            journey = journey_schedule.journeys_for_at(self.very_far_proposal.proponent, self.interval)
        except Exception as e:
            assertIs(e, NotScheduledJourney)

    def test_organizer_should_merge_similar_proposals_together_when_there_are_spare_seats(self):
        pass



if __name__ == "__main__":
    unittest.main()
