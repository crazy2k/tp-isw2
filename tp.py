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
    def __init__(self, name, day_ordinal):
        self.name = name
        self.day_ordinal = name

    def __repr__(self):
        return self.name

    def same_day(self, datetime):
        return datetime.weekday() == self.day_ordinal

    day_names = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
DayOfWeek.days_of_week = [DayOfWeek(name, number) for name, number in 
    zip(DayOfWeek.day_names, range(6))]
    


class EventOccurrence:
    def take_place_at(self, date_time):
        raise NotImplementedError()
        
class SingleTimeOccurrence:
    def __init__(self, datetime):
        self.daytime = datetime

    def take_place_at(self, datetime):
        return self.datetime == datetime


class WeeklyEventOccurrence(EventOccurrence):
    def __init__(self, time, days_of_week):
        self.days_of_week = days_of_week
        self.time = time

    def take_place_at(self, datetime):
        return any(day_of_week.same_day(datetime) for day_of_week in self.days_of_week)
        

class PhisicalEvent:
    def __init__(self, place, occurrence):
        self.place = place
        self.occurrence = occurrence


class CommuteRequest:
    #TODO: ¿La vuelta del trabajo, importa?
    def __init__(self, passenger, departure, arrival):
        self.passenger = passenger
        self.departure = departure
        self.arrival = arrival


class CommuteOffer:
    def __init__(self, driver, departure, arrival, passenger_capacity):
        self.driver = driver
        self.departure = departure
        self.arrival = arrival
        self.occurrence = occurrence
        self.passengers_capacity = passengers_capacity


class Journey:
    def __init__(self, accepted_offer, date, stops):
        self.accepted_offer = accepted_offer
        self.date = date
        self.stops = stops


class JourneyStop(PhisicalEvent):
    def __init__(self, place, ocurrence, passenger):
        PhisicalEvent.__init__(self, place, ocurrence)
        self.passenger = passenger
        
class JourneyStopForDeparture(JourneyStop):
    pass

class JourneyStopForEntrance(JourneyStop):
    pass

class JourneyOrganizer:
    def __init__(self, date, requests, offers):
        self.date = date
        self.requests = filter_by_date(requests)
        self.offers = filter_by_date(offers)

    def filter_by_date(self, events):
        return [event for event in events if event.ocurrence.take_place_at(self.date)]

    def organize(self):
        pass
