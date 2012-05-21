from bottle import route, run, view, request, response, redirect

import backend

SECRET = "ohaoha"
GRID_HEIGHT = 10
GRID_WIDTH = 15

site_backend = backend.Backend()

def set_cookie_email(email):
    response.set_cookie("email", email, secret=SECRET)

def delete_cookie_email():
    response.set_cookie("email", "")

def get_cookie_email():
    return request.get_cookie("email", secret=SECRET, default=None)

def get_currently_logged_in_user():
    email = get_cookie_email()
    return site_backend.get_logged_in_user(email, default=None)


def add_user_status(f):
    def dec(*args, **kwargs):
        result = f(*args, **kwargs)

        if isinstance(result, dict):
            email = get_cookie_email()
            user = get_currently_logged_in_user()

            result["user_status"] = {
                "logged_in": user is not None,
                "email": email
            }
        return result

    return dec

@route("/control")
def control():
    return "\n".join(dir(site_backend))
    

@route("/")
@view("index")
@add_user_status
def index():
    return {}

@route("/register")
@view("register")
@add_user_status
def register():
    return {"failed": False}

@route("/register", method="POST")
@view("register")
@add_user_status
def register_post():
    email = request.forms.get("email", None)
    passwd = request.forms.get("passwd", None)

    if not email or not passwd:
        return {"failed": True, "reason": "empty_field"}

    if not site_backend.register_user(email, passwd):
        return {"failed": True, "reason": "register_error"}

    redirect("/login")

@route("/login", method="POST")
@view("login")
@add_user_status
def login_post():
    email = request.forms.get("email", None)
    passwd = request.forms.get("passwd", None)

    if not email or not passwd:
        return {"failed": True, "reason": "empty_field"}

    if not site_backend.login_user(email, passwd):
        return {"failed": True, "reason": "auth_error"}

    set_cookie_email(email)
    redirect("/")


@route("/login")
@view("login")
@add_user_status
def login():
    return {"failed": False}


@route("/logout")
def logout():
    email = get_cookie_email()
    if site_backend.logout_user(email):
        delete_cookie_email()
    redirect("/")

@route("/createproposal/:with_or_without_vehicle")
@view("createproposal")
@add_user_status
def createproposal(with_or_without_vehicle):
    return {
        "with_vehicle": with_or_without_vehicle == "withvehicle",
        "failed": False,
        "height": GRID_HEIGHT,
        "width": GRID_WIDTH
    }

@route("/createproposal/:with_or_without_vehicle", method="POST")
@view("createproposal")
@add_user_status
def createproposal_post(with_or_without_vehicle):
    proponent = get_currently_logged_in_user()
    origin = request.forms.get("origin", None)
    destination = request.forms.get("destination", None)

    def is_checked(dayofweekname):
        return request.forms.get(dayofweekname, None) == "on"

    daysofweeknames = ["monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]
    daysofweekchecks = map(is_checked, daysofweeknames)

    atime = request.forms.get("time", None)

    if with_or_without_vehicle == "withvehicle":
        capacity = request.forms.get("capacity", None)

        worked = site_backend.create_proposal_with_vehicle(proponent, origin,
            destination, daysofweekchecks, atime, capacity)
    else:
        worked = site_backend.create_proposal_without_vehicle(proponent,
            origin, destination, daysofweekchecks, atime)

    if not worked:
        return {
            "with_vehicle": with_or_without_vehicle == "withvehicle",
            "failed": True,
            "reason": "invalid_data"
        }

    redirect("/")


@route("/viewnotifications",)
@view("viewnotifications")
@add_user_status
def viewnotifications():

    user = get_currently_logged_in_user()
    proposals_with_vehicule = \
        site_backend.get_proposals_with_vehicle_for(user)
    proposals_without_vehicule = \
        site_backend.get_proposals_without_vehicle_for(user)

    organized_journeys = site_backend.get_journeys_for(user)

    return {
        "proposals_with_vehicule": proposals_with_vehicule,
        "proposals_without_vehicule": proposals_without_vehicule,
        "organized_journeys": organized_journeys,
    }

@route("/organize", method="POST")
def organize_post():
    time_tolerance = request.forms.get("time_tolerance", None)
    distance_tolerance = request.forms.get("distance_tolerance", None)

    site_backend.organize_journeys(time_tolerance, distance_tolerance)
    redirect("/viewnotifications")


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
