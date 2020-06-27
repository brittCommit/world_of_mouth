from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


db = SQLAlchemy()


class Route(db.Model):
    """A route"""

    __tablename__ = 'routes'

    route_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    is_completed = db.Column(db.Boolean, 
                        default = False)
    trip_description = db.Column(db.String(50), 
                                nullable = False)
    trip_length = db.Column(db.Integer, default = 0)
    

    #Relationships with other tables
    stop = db.relationship('Stop')
    user = db.relationship('User')
    route_type = db.relationship('RouteType')
    favorite = db.relationship('Favorite')
 
    def __repr__(self):
        return f"""<Route id is {self.route_id} 
                by user {self.user_id} and the trip description is {self.trip_description} 
                and the route is completed{self.is_completed}>"""


class Stop(db.Model):
    """A stop"""

    __tablename__ = 'stops'

    stop_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    city_name = db.Column(db.String, 
                        nullable = False)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    created_at = db.Column(db.DateTime, 
                        default = datetime.utcnow)
    is_start = db.Column(db.Boolean, 
                        default = False)
    is_end = db.Column(db.Boolean, 
                        default = False)
    stay_length = db.Column(db.Integer)
    lat = db.Column(db.Float, 
                        nullable = False)
    lng = db.Column(db.Float, 
                        nullable = False)
    country_code = db.Column(db.String(2))
    highlights = db.Column(db.Text)

    #Relationships with other tables
    route = db.relationship('Route')

    def __repr__(self):
        return f"""<Stop #{self.stop_id} in {self.city_name} on route #{self.route_id} and is_start {self.is_start} and is_end {self.is_end}.>"""


class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    email = db.Column(db.String,
                        unique = True,
                        nullable = False)
    first_name = db.Column(db.String,
                        nullable = False)
    user_name = db.Column(db.String,
                        unique = True,
                        nullable = False)
    password = db.Column(db.String,
                        nullable = False)
    home_country = db.Column(db.String)
    image = db.Column(db.String)


    #Relationships with other tables
    route = db.relationship('Route')
    favorite = db.relationship('Favorite')

    def __repr__(self):
        return f"<User id #{self.user_id} belongs to {self.user_name} @ {self.email}.>"

class TripType(db.Model):
    """Trip Types"""

    __tablename__ = 'trip_types'

    trip_type_id = db.Column(db.Integer, 
                            autoincrement=True,
                            primary_key=True)
    trip_type = db.Column(db.String(15), nullable=False)


    #Relationships with other tables
    route_type = db.relationship('RouteType')

    def __repr__(self):
        return f"<TripType TTid is {self.trip_type_id} and trip type is {self.trip_type}>" 


class RouteType(db.Model):
    """Route Type-many to many"""

    __tablename__ = "route_types"

    route_type_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    route_id = db.Column(db.Integer, 
                        db.ForeignKey('routes.route_id'), 
                        nullable=False)
    trip_type_id = db.Column(db.Integer,
                            db.ForeignKey('trip_types.trip_type_id'),
                            nullable=False)

   #Relationships with other tables
    route = db.relationship('Route')
    trip_type = db.relationship('TripType')

    def __repr__(self):
        return f"<RouteType RTid is {self.trip_type_id} and route id is {self.route_id}>" 

class Favorite(db.Model):
    """Favorite routes"""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    route_id = db.Column(db.Integer,
                        db.ForeignKey('routes.route_id'),
                        nullable=False)

    #Relationships with other tables
    route = db.relationship('Route')
    user = db.relationship('User')

    def __repr__(self):
        return f"<Favorite is {self.favorite_id}, user is {self.user_id}, route is {self.route_id}."


def connect_to_db(flask_app, db_uri='postgresql:///routes', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)





