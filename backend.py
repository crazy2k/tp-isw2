import datetime

import tp

class Backend:
    def __init__(self):
        self.registered_users = {}
        self.logged_in_users = {}
        self.proposals = []
        self.journey_schedule = None

    def register_user(self, email, passwd):
        if self.registered_users.get(email, None):
            return False

        self.registered_users[email] = tp.User(email, passwd)
        return True

    def login_user(self, email, passwd):
        users = [user for email, user in self.registered_users.items() if
            user.authenticate(email, passwd)]

        if not len(users) == 1:
            return False
        else:
            self.logged_in_users[email] = users[0]
            return True

    def logout_user(self, email):
        if self.logged_in_users.get(email, None):
            del self.logged_in_users[email]

        return True

    def get_logged_in_user(self, email, default=None):
        return self.logged_in_users.get(email, default)

    def prepare_data_for_proposal_creation(self, proponent, origin,
        destination, daysofweekchecks, atime):

        def field_to_grid_position(data):
            data = map(int, data.split("-"))
            return tp.GridPosition(*data)

        origin = field_to_grid_position(origin)
        destination = field_to_grid_position(destination)

        days_of_week = []
        for ordinal, check in enumerate(daysofweekchecks):
            if check:
                days_of_week.append(tp.DayOfWeek.days_of_week[ordinal])

        atime = map(int, atime.split(":"))
        atime = datetime.time(*atime)

        timetable = tp.WeeklyTimetable(atime, days_of_week)

        return {
            "proponent": proponent,
            "origin": origin,
            "destination": destination,
            "timetable": timetable,
        }


    def create_proposal_with_vehicle(self, proponent, origin, destination,
        daysofweekchecks, atime, capacity):

        data = self.prepare_data_for_proposal_creation(proponent, origin,
            destination, daysofweekchecks, atime)

        proposal = tp.JourneyProposalWithVehicule(data["proponent"],
            data["origin"], data["destination"], data["timetable"],
            int(capacity))
        self.proposals.append(proposal)

        return True

    def create_proposal_without_vehicle(self, proponent, origin, destination,
        daysofweekchecks, atime):

        data = self.prepare_data_for_proposal_creation(proponent, origin,
            destination, daysofweekchecks, atime)

        proposal = tp.JourneyProposalWithoutVehicule(data["proponent"],
            data["origin"], data["destination"], data["timetable"])

        self.proposals.append(proposal)

        return True

    def prepare_proposals_for_printing(self, proponent, proposal_type):
        def is_eligible(proposal):
            return proposal.proponent == proponent and \
                isinstance(proposal, proposal_type)

        proposals = filter(is_eligible, self.proposals)

        printable_proposals = []
        for proposal in proposals:
            printable_proposal = {
                "origin": str(proposal.origin),
                "destination": str(proposal.destination),
                "daysofweeknames": [day_of_week.name for day_of_week in
                    proposal.timetable.days_of_week],
                "time": proposal.timetable.time,
            }
            if proposal_type == tp.JourneyProposalWithVehicule:
                printable_proposal["capacity"] = str(proposal.passenger_capacity)
            printable_proposals.append(printable_proposal)

        return printable_proposals

    def get_proposals_with_vehicle_for(self, proponent):
        return self.prepare_proposals_for_printing(proponent,
            tp.JourneyProposalWithVehicule)

    def get_proposals_without_vehicle_for(self, proponent):
        return self.prepare_proposals_for_printing(proponent,
            tp.JourneyProposalWithoutVehicule)

    def organize_journeys(self, time_tolerance, distance_tolerance):
        timedelta = datetime.timedelta(minutes=int(time_tolerance))
        distance_tolerance = int(distance_tolerance)
        interval_begin = datetime.datetime.now()
        interval_end = interval_begin + datetime.timedelta(days=20)
        week_interval = tp.DateTimeInterval(interval_begin, interval_end)
        organizer = tp.SimpleJourneyOrganizer(self.proposals, week_interval,
            timedelta, distance_tolerance)
        self.journey_schedule = organizer.organize()

    def get_journeys_for(self, user):
        if not self.journey_schedule:
            return []

        journeys = self.journey_schedule.journeys_for(user)

        printable_journeys = []
        for journey in journeys:
            printable_journey = {
                "driver": journey.accepted_proposal.proponent.email,
                "datetime": str(journey.datetime),
                "count": str(len(journey.people())),
                "total_seats": str(journey.total_seats()),
                "starting_point": str(journey.start_point()),
                "end_point": str(journey.end_point()),
            }
            printable_journeys.append(printable_journey)
        return printable_journeys

