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
    day_names = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

    def __init__(self, name, ordinal):
        self.name = name
        self.ordinal = ordinal

    def __repr__(self):
        return self.name

    def __lt__(self, other_week_day):
        return self.ordinal < other_week_day.ordinal

    def same_day_as(self, adatetime):
        return adatetime.weekday() == self.ordinal

DayOfWeek.days_of_week = tuple(DayOfWeek(name, number) for number, name in
    enumerate(DayOfWeek.day_names))


class Timetable: # Or Schedule (both are more or less synonyms)
    def is_happening_at(self, adatetime):
        raise NotImplementedError()

    def is_during_this_date(self, adate):
        raise NotImplementedError()

class SingleTimeTimetable(Timetable):
    def __init__(self, datetime):
        self.daytime = datetime

    def is_happening_at(self, adatetime):
        return self.datetime == adatetime

    def is_during_this_date(self, adate):
        return self.datetime.date() == adate

class RepetitiveTimetable(Timetable):
    pass

class WeeklyTimetable(RepetitiveTimetable):
    def __init__(self, atime, days_of_week):
        self.days_of_week = days_of_week
        self.time = atime

    def is_happening_at(self, adatetime):
        return any(day_of_week.same_day_as(adatetime) and datetime.time() == self.time for day_of_week in self.days_of_week)

    def is_during_this_date(self, adatetime):
        return any(day_of_week.same_day_as(adatetime) for day_of_week in self.days_of_week)


class JourneyRequest:
    #TODO: ¿La vuelta del trabajo, importa?
    def __init__(self, passenger, origin, destination, timetable):
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.timetable = timetable

    def plausible_offers(offers):
        return [offer for offer in offers if offer.satisfies(request)]

# TODO: ¿Crear siempre una JourneyRequest por cada JourneyOffer asi el usuario q ofrece su auto tambien
#       es tenido en cuenta para otras ofertas de auto que no sean iniciadas por el?
class JourneyOffer:
    def __init__(self, driver, origin, destination, timetable, passenger_capacity):
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.timetable = timetable
        self.passengers_capacity = passengers_capacity

    def satisfies(request):
        return self.is_on_its_way(request.origin) and offer.is_on_its_way(request.destination)

    def is_on_its_way(place): #TODO
        pass


class Journey:
    def __init__(self, accepted_offer, date, stops):
        self.accepted_offer = accepted_offer
        self.date = date
        self.stops = stops


class JourneyStop:
    def __init__(self, place, datetime, passengers):
        self.place = place
        self.datetime = datetime
        self.passengers = passengers


class JourneyStopForBoarding(JourneyStop):
    pass


class JourneyStopForDischarging(JourneyStop):
    pass


class JourneyOrganizer:
    def __init__(self, date, tolerance, requests, offers):
        self.date = date
        self.tolerance = tolerance #Late tolerance as a lapse of time (some minutes/hours)
        self.requests = filter_by_date(requests)
        self.offers = filter_by_date(offers)

    def filter_by_date(self, schedulables):
        return [schedulable for schedulable in schedulables if schedulable.timetable.is_during_this_date(self.date)]

    def plausible_offers_for(request):
        return request.plausible_offers(self.offers)

    def organize(self):
        pass

class Notification:
    pass

class UnsuccesfulMatchNotification(Notification):
    def __init__(self, request):
        self.request = request

class SuccesfulMatchNotification(Notification):
    def __init__(self, request, journey, journey_stop):
        self.request = request
        self.journey = journey
        self.journey_stop = journey_stop


class NotificationSender:
    def send_mail(notification):
        pass
