"""CRUD operations"""

from model import db, User, Route, Stop, TripType, RouteType, connect_to_db

if __name__=='__main__':
    from server import app
    connect_to_db(app)
    db.create_all()


def create_user(email, first_name, user_name, password, home_country):
    """Create and return a new user."""

    user = User(email = email, 
                first_name = first_name,
                user_name = user_name, 
                password = password, 
                home_country = home_country)

    db.session.add(user)
    db.session.commit()

    return user


def create_route(user, trip_description):
    """Create and return a new route."""

    route = Route(user = user,
                  trip_description= trip_description)

    db.session.add(route)
    db.session.commit()

    return route

def create_stop(city_name, route, stay_length, lat, lng, country_code, is_start, is_end):
    
    stop = Stop(city_name = city_name,
                route = route, 
                stay_length = stay_length,
                lat = lat,
                lng = lng,
                country_code = country_code,
                is_start = is_start,
                is_end = is_end)

    if stop.is_end == True:
        route.is_completed = True

    route.trip_length += stop.stay_length

    db.session.add(stop)
    db.session.commit()

    return stop

def create_trip_type(trip_type):

    trip_type = TripType(trip_type = trip_type)

    db.session.add(trip_type)
    db.session.commit()

    return trip_type

def create_route_type(route_id, trip_type_id):

    route_type = RouteType(route_id = route_id, 
                        trip_type_id = trip_type_id)
    
    db.session.add(route_type)
    db.session.commit()

    return route_type

def get_user_by_id(user_id):
    """Return a user associated with a user_id"""

    return User.query.get(user_id)


def get_user_by_email(email): 

    return User.query.filter(User.email == email).first()


def get_routes():
    """Get all routes"""

    return Route.query.all()


def get_route_by_id(route_id):
    """Return a route associated with a user_id"""

    return Route.query.get(route_id)


def get_routes_by_user(user_id):

    return Route.query.filter(Route.user_id == user_id).all()


def get_stops():
    """Get all stops"""

    return Stop.query.all()


def get_stops_by_route_id(route_id):
    """Get stops associated with a particular route id"""

    return Stop.query.filter(Stop.route_id == route_id).all()


def get_is_end_by_route_id(route_id):
    """Get the last stop assigned to a route_id"""

    return Stop.query.filter((Stop.route_id == route_id) & (Stop.is_end == True)).all()


def get_is_start_by_route_id(route_id):
    """Get the last stop assigned to a route_id"""

    return Stop.query.filter((Stop.route_id == route_id) & (Stop.is_start == True)).all()
    

def create_stop_dict(stop):
    """Make a dictionary to pass through a route using json"""

    stop_dict = {"city_name": stop.city_name,
                "is_start": stop.is_start,
                "is_end": stop.is_end,
                "route_id": stop.route_id,
                "stay_length": stop.stay_length,
                "lat": stop.lat,
                "lng":stop.lng,
                "country_code": stop.country_code
                }

    return stop_dict


def get_stops_by_country_code(country_code):
    """Return all routes trip descriptions containing a stop with requested country code"""

    return Stop.query.filter(Stop.country_code == country_code).all()


def get_all_routes_with_stop_with_country_code(country_code):
    """ Return all routes that contain a stop in a given country"""

    return db.session.query(Route).join(Stop).filter(Stop.country_code == country_code).all()


# def get_routes_with_stop():
#     """Return routes with requested cities"""

