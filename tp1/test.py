import unittest

from tp import *


class StubedAddressWebService(AddressWebService):
    @classmethod
    def distance_from_to(cls, addr1, addr2):
        return True

class UserTests(unittest.TestCase):
    def test_init(self):
        user = User("pablo@pablo.com", "123456")

        self.assertEqual("pablo@pablo.com", user.email)
        self.assertEqual("123456", user.passwd)

class DayOfWeekTests(unittest.TestCase):
    def test_init(self):
        lunes = DayOfWeek("Lunes")

        self.assertEqual("Lunes", lunes.name)

    def test_lt(self):
        self.assertTrue(MONDAY < TUESDAY)

class JourneyStopTests():
    def setUp(self):
        self.where = Place()
        self.passengers = [User("pablo@pablo.com", "123456")]

    def test_init(self):
        stop = JourneyStop(self.where, self.passengers, [])

        self.assertEqual(self.where, stop.place)
        self.assertEqual(self.passengers, stop.passengers_stepping_in)
        self.assertEqual([], stop.passengers_leaving)

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.user = User("pablo@pablo.com", "123456")


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
    def get_proposal_with_car(self):
        proponent = User("pablo@pablo.com", "123456")
        address1 = Address("Rivadavia 6242")
        address2 = Address("Viamonte 1203")
        timetable = WeeklyTimetable(time(8, 30), (MONDAY,))
        return JourneyProposalWithVehicule(proponent, address1, address2,
            timetable, 2)

    def get_proposal_without_car(self):
        proponent = User("rodrigo@rodrigo.com", "654321")
        address1 = Address("Rivadavia 6486")
        address2 = Address("Viamonte 1205")
        timetable = WeeklyTimetable(time(8, 25), (MONDAY,))
        return JourneyProposalWithoutVehicule(proponent, address1, address2,
            timetable)

    def get_another_proposal_with_car(self):
        proponent = User("ashy@ashy.com", "123456")
        address1 = Address("Rivadavia 6205")
        address2 = Address("Viamonte 1305")
        timetable = WeeklyTimetable(time(8, 30), (MONDAY,))
        return JourneyProposalWithVehicule(proponent, address1, address2,
            timetable, 3)

    def get_very_far_proposal_with_car(self):
        proponent = User("pablo@pablo.com", "123456")
        address1 = GridPosition(0,0)
        address2 = GridPosition(5000,5000)
        timetable = WeeklyTimetable(time(8, 30), (MONDAY,))
        return JourneyProposalWithVehicule(proponent, address1, address2,
            timetable, 2)

    def get_very_far_proposal_with_no_car(self):
        proponent = User("rodrigo@rodrigo.com", "654321")
        address1 = GridPosition(8000,8000)
        address2 = GridPosition(1000,1000)
        timetable = WeeklyTimetable(time(8, 25), (MONDAY,))
        return JourneyProposalWithoutVehicule(proponent, address1, address2,
            timetable)



    def setUp(self):
        Address.web_service = StubedAddressWebService

        self.time_tolerance = timedelta(minutes=15)
        self.week_interval = DateTimeInterval(datetime(2012, 5, 14), datetime(2012, 5, 19))
        self.distance_tolerance = 300

        self.proposal_with_car = self.get_proposal_with_car()
        self.proposal_without_car = self.get_proposal_without_car()
        self.another_proposal_with_car = self.get_another_proposal_with_car()

        self.very_far_proposal_with_car = self.get_very_far_proposal_with_car()
        self.very_far_proposal_with_no_car = self.get_very_far_proposal_with_no_car()


        self.proposals = [self.proposal_with_car, self.proposal_without_car]
        self.proposals_with_many_cars = [self.proposal_with_car, self.proposal_without_car, self.another_proposal_with_car]
        self.proposals_too_far_from_each_other = [self.very_far_proposal_with_car, self.very_far_proposal_with_no_car]

        self.organizer = SimpleJourneyOrganizer(self.time_tolerance, self.distance_tolerance)


    def test_organizer_should_create_journey_for_compatible_proposals(self):
        journey_schedule = self.organizer.organize(self.proposals, self.week_interval)

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
        self.assertTrue(abs(delta.total_seconds()) <= self.time_tolerance.total_seconds())

        self.assertEqual(journey.datetime.date(), journey.date())

        
    def test_organizer_should_notify_when_a_proposal_was_not_posible_to_organize(self):
        journey_schedule = self.organizer.organize(self.proposals_too_far_from_each_other, self.week_interval)

        self.assertEqual(1, journey_schedule.total_journeys())

        when = self.very_far_proposal_with_car.timetable.ocurrences_at(self.week_interval)[0]

        journey = journey_schedule.journey_for_at(self.very_far_proposal_with_car.proponent, when)

        self.assertEqual(self.very_far_proposal_with_car, journey.accepted_proposal)

        try:
            when = self.very_far_proposal_with_no_car.timetable.ocurrences_at(self.week_interval)[0]
            journey = journey_schedule.journey_for_at(self.very_far_proposal_with_no_car.proponent, when)
        except Exception as e:
            self.assertIsInstance(e, NotScheduledJourney)

    def test_organizer_should_merge_similar_proposals_together_when_there_are_spare_seats(self):
        journey_schedule = self.organizer.organize(self.proposals_with_many_cars, self.week_interval)

        journey = journey_schedule.journeys_for(self.proposal_with_car.proponent)[0]

        self.assertEqual(1, journey_schedule.total_journeys())
        self.assertEqual(self.another_proposal_with_car, journey.accepted_proposal)

        self.assertTrue(self.proposal_with_car.proponent in journey.people())
        self.assertTrue(self.proposal_without_car.proponent in journey.people())
        self.assertTrue(self.another_proposal_with_car.proponent in journey.people())


if __name__ == "__main__":
    unittest.main()
