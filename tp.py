# coding: utf8

from datetime import datetime,date,time,timedelta
from functools import reduce
from itertools import groupby, chain
from math import sqrt

class User:
    """Represents a registered user."""
    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd


class Place:
    def is_near(self, place, tolerance):
        return self.distance_to(place) <= tolerance

    def distance_to(self, place):
        """Returns distance between two places in meters"""
        raise NotImplementedError()

class GridPosition(Place):
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def distance_to(self, place):
        x_2 = abs(place.x_coordinate - self.x_coordinate) ** 2
        y_2 = abs(place.y_coordinate - self.y_coordinate) ** 2
        return sqrt(x_2 + y_2)

    def __str__(self):
        return "(%d, %d)" % (self.x_coordinate, self.y_coordinate)

class Address(Place):
    def __init__(self, street):
        self.street = street

    def distance_to(self, other_address):
        return self.web_service.distance_from_to(self, other_address)

class AddressWebService:
    @classmethod
    def distance_from_to(cls, address1, address2):
        raise NotImplementedError()

class DayOfWeek:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __lt__(self, other_week_day):
        return self.ordinal() < other_week_day.ordinal()

    def same_day_as(self, adatetime):
        return adatetime.weekday() == self.ordinal()

    def ordinal(self):
        return self.days_of_week.index(self)

    @classmethod
    def at(cls, adatetime):
        return cls.days_of_week[adatetime.weekday()]

MONDAY    = DayOfWeek("Lunes")
TUESDAY   = DayOfWeek("Martes")
WEDNESDAY = DayOfWeek("Miercoles")
THURSDAY  = DayOfWeek("Jueves")
FRIDAY    = DayOfWeek("Viernes")
SATURDAY  = DayOfWeek("Sábado")
SUNDAY    = DayOfWeek("Domingo")

DayOfWeek.days_of_week = (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)

class DateTimeInterval:
    def __init__(self, begin, end):
        if begin > end:
            raise ValueError("Begin must be before end")

        self._begin = begin
        self._end = end

    def begin(self):
        return self._begin

    def end(self):
        return self._end

    def overlaps(self, adatetime):
        return self._begin <= adatetime < self._end

    def included_days(self):
        first = self._begin.date()
        last = self._end.date()
        days = [first + timedelta(days=1) * offset
            for offset in range((last-first).days - 1)]

        return days

class Timetable: # Or Schedule (both are more or less synonyms)
    def ocurrences_at(self, interval):
        raise NotImplementedError()

    def times_within_inverval(self, interval):
        return len(self.ocurrences_within_interval(interval))

    def happens_within_inverval(self, interval):
        return self.times_within_inverval(interval) > 0


class SingleTimeTimetable(Timetable):
    def __init__(self, adatetime):
        self.daytime = adatetime

    def ocurrences_at(self, interval):
        if interval.overlaps(self.daytime):
            return [self.daytime]
        else:
            return []

class RepetitiveTimetable(Timetable):
    pass

class WeeklyTimetable(RepetitiveTimetable):
    def __init__(self, atime, days_of_week):
        self.days_of_week = days_of_week
        self.time = atime

    def ocurrences_at(self, interval):
        timetable_datetimes = [datetime.combine(adate, self.time) for adate in interval.included_days()]
        
        def included_datetime(adatetime):
            return interval.overlaps(adatetime) and DayOfWeek.at(adatetime) in self.days_of_week

        return list(filter(included_datetime, timetable_datetimes))


class JourneyProposal:
    def __init__(self, proponent, origin, destination, timetable):
        self.proponent = proponent
        self.origin = origin
        self.destination = destination
        self.timetable = timetable

    def has_vehicule(self):
        raise NotImplementedError()



class JourneyProposalWithVehicule(JourneyProposal):
    def __init__(self, proponent, origin, destination, timetable, passenger_capacity):
        super().__init__(proponent, origin, destination, timetable)
        self.passenger_capacity = passenger_capacity

    def has_vehicule(self):
        return True

class JourneyProposalWithoutVehicule(JourneyProposal):
    def has_vehicule(self):
        return False


class Journey:
    def __init__(self, accepted_proposal, adatetime, stops):
        self.accepted_proposal = accepted_proposal
        self.stops = stops
        self.datetime = adatetime

    @classmethod
    def from_proposal_at(cls, proposal, adatetime):
        stops = [JourneyStop(place, [], []) for place in [proposal.origin, proposal.destination]]
        journey = Journey(proposal, adatetime, stops)
        journey.add_passenger(proposal.proponent)

        return journey

    @classmethod
    def create_journeys_for_proposal(cls, proposal, interval):
        journeys = []
        for adatetime in proposal.timetable.ocurrences_at(interval):
            journeys.append(cls.from_proposal_at(proposal, adatetime))

        return journeys


    def can_be_merged_with(self, other_journey, time_tolerance, distance_tolerance):
        return self.satisfies_proposal_at(other_journey.accepted_proposal, other_journey.datetime, time_tolerance, distance_tolerance)

    def satisfies_proposal_at(self, proposal, adatetime, time_tolerance, distance_tolerance):
        is_near = self.start_point().is_near(proposal.origin, distance_tolerance) and \
            self.end_point().is_near(proposal.destination, distance_tolerance) 

        is_close_in_time = abs((self.datetime - adatetime).total_seconds()) <= time_tolerance.total_seconds()

        return is_near and is_close_in_time


    def people(self):
        return reduce(set.union, [set(stop.passengers_stepping_in) for stop in self.stops])

    def date(self):
        return self.datetime.date()

    def total_seats(self):
        return self.accepted_proposal.passenger_capacity

    def spare_seats(self):
        return self.total_seats() - len(self.people())

    def has_spare_seats(self):
        return self.spare_seats() > 0

    def start_point(self):
        return self.stops[0].place

    def end_point(self):
        return self.stops[-1].place

    def add_passenger(self, passenger):
        self.stops[0].add_passenger_stepping_in(passenger)
        self.stops[-1].add_passenger_leaving(passenger)

    def remove_passenger(self, passenger):
        self.stops[0].remove_passenger_stepping_in(passenger)
        self.stops[-1].remove_passenger_leaving(passenger)

    def move_passengers_to(self, other_journey):
        for passenger in self.people():
            if other_journey.has_spare_seats():
                other_journey.add_passenger(passenger)
                self.remove_passenger(passenger)

    
class JourneyStop:
    def __init__(self, place, passengers_stepping_in, passengers_leaving):
        self.place = place
        self.passengers_stepping_in = passengers_stepping_in
        self.passengers_leaving = passengers_leaving

    def remove_passenger_stepping_in(self, passenger):
        self.passengers_stepping_in.remove(passenger)

    def remove_passenger_leaving(self, passenger):
        self.passengers_leaving.remove(passenger)

    def add_passenger_stepping_in(self, passenger):
        self.passengers_stepping_in.append(passenger)

    def add_passenger_leaving(self, passenger):
        self.passengers_leaving.append(passenger)


class JourneyOrganizer:
    def organize(self):
        raise NotImplementedError()

class SimpleJourneyOrganizer(JourneyOrganizer):
    def __init__(self, proposals, interval, time_tolerance, distance_tolerance):
        self.proposals = proposals
        self.interval = interval
        self.time_tolerance = time_tolerance #Late tolerance as a lapse of time (some minutes/hours)
        self.distance_tolerance = distance_tolerance

        self.proposals_with_vehicule = [proposal for proposal in proposals if proposal.has_vehicule()]
        self.proposals_without_vehicule = [proposal for proposal in proposals if not proposal.has_vehicule()]

        self.results = []

    def plausible_offers_for(self, request):
        return request.plausible_offers(self.offers)

    def organize(self):
        self.create_journeys_for_proposals_with_vehicule()
        self.match_proposals_with_journeys()
        self.optimize_results()

        return JourneySchedule(self.results)

    def create_journeys_for_proposals_with_vehicule(self):
        def journeys_for(proposal):
            return Journey.create_journeys_for_proposal(proposal, self.interval)

        self.results = list(chain(*map(journeys_for, self.proposals_with_vehicule)))

    def match_proposals_with_journeys(self):
        self.results.sort(key=Journey.total_seats, reverse=True)

        for proposal in self.proposals_without_vehicule:
            for adatetime in proposal.timetable.ocurrences_at(self.interval):

                def is_candidate(candidate):
                    return candidate.satisfies_proposal_at(proposal, adatetime, self.time_tolerance, self.distance_tolerance) \
                        and candidate.has_spare_seats()    
                journeys = list(filter(is_candidate, self.results))
                
                if len(journeys) > 0:
                    journeys[0].add_passenger(proposal.proponent)

    def optimize_results(self):
        self.results.sort(key=lambda journey: len(journey.people()))
        other_journeys = self.results[:] #Duplicate list

        for journey in self.results:
            other_journeys.remove(journey)
            other_journeys = list(filter(Journey.has_spare_seats, other_journeys))
            other_journeys.sort(key=Journey.spare_seats)
            other_journeys.sort(key=Journey.total_seats, reverse=True)

            def is_compatible(other_journey):
                return journey.can_be_merged_with(other_journey, self.time_tolerance, self.distance_tolerance) 

            for other_journey in filter(is_compatible, other_journeys):
                journey.move_passengers_to(other_journey)

        self.results = [journey for journey in self.results if len(journey.people()) > 0]


class JourneySchedule:
    def __init__(self, journeys = []):
        self.journeys = set([])

        for journey in journeys:
            self.add_journey(journey)

    def add_journey(self, journey):
        self.journeys.add(journey)

    def total_journeys(self):
        return len(self.journeys)

    def journeys_for(self, user):
        return [journey for journey in self.journeys if user in journey.people()]

    def journey_for_at(self, user, adatetime):
        journeys = [journey for journey in self.journeys_for(user) if journey.datetime == adatetime]

        if len(journeys) == 0:
            raise NotScheduledJourney()

        return journeys[0]

class NotScheduledJourney(Exception):
    pass

class Notification:
    def content(self):
        raise NotImplementedError()

    @classmethod
    def notifications_for_at(journey_schedule, proposal, interval):
        result = []
        for adatetime in proposal.timetable.ocurrences_at(interval):
            try:
                journey = journey.journey_for_at(proposal.proponent, adatetime)
                result.append(SuccesfulMatchNotification(proposal, journey))
            except NotScheduledJourney:
                result.append(UnsuccesfulMatchNotification(proposal))

        return result

class UnsuccesfulMatchNotification(Notification):
    def __init__(self, proposal):
        self.proposal = proposal

    def content(self):
        pass

class SuccesfulMatchNotification(Notification):
    def __init__(self, proposal, journey):
        self.proposal = proposal
        self.journey = journey

    def content(self):
        pass


class NotificationSender:
    def send_mail(self, notification):
        pass
