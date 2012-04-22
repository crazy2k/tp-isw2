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

    def same_day(self, adatetime):
        return adatetime.weekday() == self.ordinal

DayOfWeek.days_of_week = tuple(DayOfWeek(name, number) for number, name in
    enumerate(DayOfWeek.day_names))


class Temporality:
    def is_happening_at(self, date_time):
        raise NotImplementedError()


class SingleTimeTemporality(Temporality):
    def __init__(self, datetime):
        self.daytime = datetime

    def is_happening_at(self, adatetime):
        return self.datetime == adatetime

class RepetitiveTemporality(Temporality):
    pass

class WeeklyTemporality(RepetitiveTemporality):
    def __init__(self, time, days_of_week):
        self.days_of_week = days_of_week
        self.time = time

    def is_happening_at(self, adatetime):
        return any(day_of_week.same_day(adatetime) for day_of_week in self.days_of_week)


class ScheduledEvent:
    def __init__(self, place, temporality):
        self.place = place
        self.temporality = temporality

    def takes_place_at(self, place):
        return self.place == place

    def is_happening_at(self, adatetime):
        return self.temporality.is_happening_at(adatetime)


class JourneyRequest:
    #TODO: ¿La vuelta del trabajo, importa?
    def __init__(self, passenger, departure, arrival):
        self.passenger = passenger
        self.departure = departure
        self.arrival = arrival


class JourneyOffer:#TODO: TransportOffer?
    def __init__(self, driver, departure, arrival, passenger_capacity):
        self.driver = driver
        self.passengers_capacity = passengers_capacity
        self.departure = departure
        self.arrival = arrival


class Journey:
    def __init__(self, accepted_offer, date, stops):
        self.accepted_offer = accepted_offer
        self.date = date
        self.stops = stops


class JourneyStop:
    def __init__(self, place, datetime, passenger):
        self.place = place
        self.datetime = datetime
        self.passenger = passenger


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

    def filter_by_date(self, events):
        return [event for event in events if event.ocurrence.is_happening_at(self.date)]

    def organize(self):
        pass

class Notification:
    pass


class NotificationSender:
	def send_mail(notification):
		pass
