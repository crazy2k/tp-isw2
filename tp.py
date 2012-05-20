# coding: utf8

from datetime import datetime

class User:
    """Represents a registered user."""
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Place:
    def distance_to(self, place):
        """Returns distance between two places in meters"""
        raise NotImplementedError()

class Address(Place):
    pass

class DayOfWeek:
    def __init__(self, name, ordinal):
        self.name = name
        self.ordinal = ordinal

    def __repr__(self):
        return self.name

    def __lt__(self, other_week_day):
        return self.ordinal < other_week_day.ordinal

    def same_day_as(self, adatetime):
        return adatetime.weekday() == self.ordinal

MONDAY    = DayOfWeek("Lunes",0)
TUESDAY   = DayOfWeek("Martes",1)
WEDNESDAY = DayOfWeek("Miercoles",2)
THURSDAY  = DayOfWeek("Jueves",3)
FRIDAY    = DayOfWeek("Viernes",4)
SATURDAY  = DayOfWeek("Sábado",5)
SUNDAY    = DayOfWeek("Domingo",6)

DayOfWeek.days_of_week = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY] 


class Timetable: # Or Schedule (both are more or less synonyms)
    def is_happening_at(self, adatetime):
        raise NotImplementedError()

    def is_during_this_date(self, adate):
        raise NotImplementedError()

    def happens_within_delta(self, timetable, delta):
        raise NotImplementedError()


class SingleTimeTimetable(Timetable):
    def __init__(self, datetime):
        self.daytime = datetime

    def is_happening_at(self, adatetime):
        return self.datetime == adatetime

    def is_during_this_date(self, adate):
        return self.datetime.date() == adate

    def happens_within_delta(self, timetable, delta):
        return timetable.happens_within_delta_for_single_time_timetable(self, tolerance)

    def happens_within_delta_for_single_time_timetable(self, timetable, delta):
        return timetable.happens_within_delta_for_single_time_timetable(self, tolerance)

class RepetitiveTimetable(Timetable):
    pass

class WeeklyTimetable(RepetitiveTimetable):
    def __init__(self, atime, days_of_week):
        self.days_of_week = days_of_week
        self.time = atime

    def is_happening_at(self, adatetime):
        return any(day_of_week.same_day_as(adatetime) and \
			datetime.time() == self.time for day_of_week in self.days_of_week)

    def is_during_this_date(self, adatetime):
        return any(day_of_week.same_day_as(adatetime) for day_of_week in self.days_of_week)

    def happens_within_delta(self, timetable, delta):
        return timetable.happens_within_delta_for_weakly_timetable(self, tolerance)


class JourneyProposal:
    def __init__(self, proponent, origin, destination, timetable):
        self.proponent = proponent
        self.origin = origin
        self.destination = destination
        self.timetable = timetable

    def has_vehicule:
        raise NotImplementedError()

    def plausible_offers(self, offers):
        return [offer for offer in offers if offer.satisfies(request)]


class JourneyProposalWithVehicule(JourneyProposal):
    def __init__(self, proponent, origin, destination, timetable, passenger_capacity):
        super().__init__(proponent, origin, destination, timetable)
        self.passenger_capacity = passenger_capacity

    def has_vehicule:
        return True


class JourneyProposalWithoutVehicule(JourneyProposal):
    def has_vehicule:
        return False
        
        

# TODO: ¿Crear siempre una JourneyRequest por cada JourneyOffer asi el usuario q ofrece su auto tambien
#       es tenido en cuenta para otras ofertas de auto que no sean iniciadas por el?
class JourneyOffer:
    def __init__(self, proponent, origin, destination, timetable, passenger_capacity):
        self.proponent = proponent
        self.origin = origin
        self.destination = destination
        self.timetable = timetable
        self.passenger_capacity = passenger_capacity

    def satisfies(self, request):
        return self.is_on_its_way(request.origin) and offer.is_on_its_way(request.destination)

    def is_on_its_way(self, place): #TODO
        pass


class Journey:
    def __init__(self, accepted_offer, date, stops):
        self.accepted_proposal = accepted_proposal
        self.date = date
        self.stops = stops


class JourneyStop:
    def __init__(self, place, datetime, passengers_stepping_in, passengers_leaving):
        self.place = place
        self.datetime = datetime
        self.passengers_stepping_in = passengers_stepping_in
        self.passengers_leaving = passengers_leaving


class JourneyOrganizer:
    def __init__(self, time_tolerance, proposals):
        self.time_tolerance = time_tolerance #Late tolerance as a lapse of time (some minutes/hours)
        self.proposal = proposals

    def plausible_offers_for(self, request):
        return request.plausible_offers(self.offers)

    def organize(self):
        pass

class Notification:
    def content(self):
        raise NotImplementedError()

class UnsuccesfulMatchNotification(Notification):
    def __init__(self, request):
        self.request = request

    def content(self):
        pass

class SuccesfulMatchNotification(Notification):
    def __init__(self, request, journey, journey_stop):
        self.request = request
        self.journey = journey
        self.journey_stop = journey_stop

    def content(self):
        pass


class NotificationSender:
    def send_mail(self, notification):
        pass
