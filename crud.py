"""CRUD operations"""

from model import db, User, Route, Stop, connect_to_db

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

def create_stop(city_name, route, created_at, is_start, is_end, stay_length, lat, lng):
    
    stop = Stop(city_name = city_name,
                route = route, 
                created_at = created_at,
                is_start = is_start,
                is_end = is_end,
                stay_length = stay_length,
                lat = lat,
                lng = lng)

    db.session.add(stop)
    db.session.commit()

    return stop


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

    return Stop.query.filter(Stop.route_id == route_id).all()

def get_route_by_id_jsonify(route_id):

    return

    

# def get_routes_with_stop():
#     """Return routes with requested cities"""

