import datetime

import tp

class Backend:
    def __init__(self):
        self.registered_users = {}
        self.logged_in_users = {}
        self.proposals = []

    def register_user(self, email, passwd):
        if self.registered_users.get(email, None):
            return False

        self.registered_users[email] = tp.User(email, passwd)
        return True

    def login_user(self, email, passwd):
        registered_user = self.registered_users.get(email)
        if not registered_user:
            return False

        if registered_user.passwd == passwd:
            self.logged_in_users[email] = registered_user
            return True

        return False

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

