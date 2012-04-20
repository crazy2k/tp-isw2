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
        

class WeeklyEventOccurrence:
    #TODO: Arreglar lo del departure_time y arrival_time
    def __init__(self, departure_time, arrival_time, day_of_week):
        self.day_of_week = day_of_week
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def take_place_at(self, datetime):
        return self.day_of_week.same_day(datetime)
        

class CommuteOffer:
    def __init__(self, driver, origin, destination, occurrence, passenger_capacity):

        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.occurrence = occurrence
        self.passengers_capacity = passengers_capacity


class CommuteRequest:
    def __init__(self, passenger, origin, destination, occurrence):

        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.occurrence = occurrence


class Journey:
    def __init__(self, accepted_offer, date, stops):
        self.accepted_offer = accepted_offer
        self.date = date
        self.stops = stops


class JourneyStop:
    def __init__(self, place, time, passenger):
        self.place = place
        self.time = time
        self.passenger = passenger
        
class JourneyStopForDeparture(CommuteStop):
    pass

class JourneyStopForEntrance(CommuteStop):
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
