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
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __lt__(self, other_week_day):
        return self.ordinal() < other_week_day.ordinal()

    def same_day_as(self, adatetime):
        return adatetime.weekday() == self.ordinal()

    def ordinal(self):
        return days_of_week.index(self)

MONDAY    = DayOfWeek("Lunes")
TUESDAY   = DayOfWeek("Martes")
WEDNESDAY = DayOfWeek("Miercoles")
THURSDAY  = DayOfWeek("Jueves")
FRIDAY    = DayOfWeek("Viernes")
SATURDAY  = DayOfWeek("Sábado")
SUNDAY    = DayOfWeek("Domingo")

DayOfWeek.days_of_week = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY] 

class TimeInterval:
    def __init__(self, begin, end):
        #TODO: Validacion: begin < end
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
    def happens_this_date(self, adate):
        raise NotImplementedError()

    def ocurrences_within_interval(self, interval):
        raise NotImplementedError()

    def times_within_inverval(self, interval):
        return len(self.ocurrences_within_interval(interval))

    def happens_within_inverval(self, interval):
        return self.times_within_inverval(interval) > 0


class SingleTimeTimetable(Timetable):
    def __init__(self, datetime):
        self.daytime = datetime

    def ocurrences_within_interval(self, interval):
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

    def ocurrences_within_interval(self, interval):
        datetimes = [datetime.combine(adate, self.time) for adate in interval.included_days()]
                    map(date => datetime.combine(adate, self.time), interval.included_days())
        
        def valid_datetime(adatetime):
            return interval.begin() <= adatetime < interval.end() and
                any(weekday.same_day_as(adatime) for weekday in self.weekdays)

        return filter(valid_datetime, datimes)


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
