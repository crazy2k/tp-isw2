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

    def create_proposal_with_vehicle(self, proponent, origin, destination,
        daysofweekchecks, atime, capacity):

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

        proposal = tp.JourneyProposalWithVehicule(proponent, origin,
            destination, timetable, int(capacity))
        self.proposals.append(proposal)

        return True

