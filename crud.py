"""CRUD operations"""

from model import db, User, Route, Stop, connect_to_db, db

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


def create_route(user, is_completed):
    """Create and return a new route."""

    route = Route(user = user,
                  is_completed= is_completed,)

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

def get_routes():
    """Get all routes"""

    return Route.query.all()


def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_route_by_id(route_id):

    return User.query.get(route_id)

# def get_routes_with_stop():
#     """Return routes with requested cities"""

