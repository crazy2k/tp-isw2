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

    def same_day(self, datetime):
        return datetime.weekday() == self.ordinal

DayOfWeek.days_of_week = tuple(DayOfWeek(name, number) for number, name in
    enumerate(DayOfWeek.day_names))


class Periodicity:
    def is_happening_at(self, date_time):
        raise NotImplementedError()


class SingleTimePeriodicity(Periodicity):
    def __init__(self, datetime):
        self.daytime = datetime

    def is_happening_at(self, adatetime):
        return self.datetime == adatetime


class WeeklyPeriodicity(Periodicity):
    def __init__(self, time, days_of_week):
        self.days_of_week = days_of_week
        self.time = time

    def is_happening_at(self, adatetime):
        return any(day_of_week.same_day(adatetime) for day_of_week in self.days_of_week)


class ScheduledEvent:
    def __init__(self, place, periodicity):
        self.place = place
        self.periodicity = periodicity

    def takes_place_at(self, place):
        return self.place == place

    def is_happening_at(self, adatetime):
        return self.periodicity.is_happening_at(adatetime)


class CommuteRequest:
    #TODO: ¿La vuelta del trabajo, importa?
    def __init__(self, passenger, departure, arrival):
        self.passenger = passenger
        self.departure = departure
        self.arrival = arrival


class CommuteOffer:#TODO: TransportOffer?
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


class JourneyStop(ScheduledEvent):
    def __init__(self, place, ocurrence, passenger):
        super().__init__(place, ocurrence)
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
