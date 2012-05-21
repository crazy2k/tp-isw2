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

@route("/createproposalwithvehicle")
@view("createproposalwithvehicle")
@add_user_status
def createproposalwithvehicle():
    return {"failed": False, "height": GRID_HEIGHT, "width": GRID_WIDTH}

@route("/createproposalwithvehicle", method="POST")
@view("createproposalwithvehicle")
@add_user_status
def createproposalwithvehicle_post():
    proponent = get_currently_logged_in_user()
    origin = request.forms.get("origin", None)
    destination = request.forms.get("destination", None)

    def is_checked(dayofweekname):
        return request.forms.get(dayofweekname, None) == "on"

    daysofweeknames = ["monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]
    daysofweekchecks = map(is_checked, daysofweeknames)

    atime = request.forms.get("time", None)
    capacity = request.forms.get("capacity", None)

    if not site_backend.create_proposal_with_car(proponent, origin,
        destination, daysofweekchecks, atime, capacity):
        return {"failed": True, "reason": "invalid_data"}

    redirect("/")



if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
