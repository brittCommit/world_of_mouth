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
    

    #Relationships with other tables
    stop = db.relationship('Stop')
    # country = db.relationship('Country')
    user = db.relationship('User')
 
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


    #Relationships with other tables
    route = db.relationship('Route')

    def __repr__(self):
        return f"<User id #{self.user_id} belongs to {self.user_name} @ {self.email}.>"

# class TripType(db.Model):
#     """Trip Types"""

#     __tablename__ = 'trip_types'

#     solo = db.Column(db.Boolean,
#               default=False)
#     group = db.Column(db.Boolean,
#               default=False)
#     couples = db.Column(db.Boolean,
#               default=False)
#     food = db.Column(db.Boolean,
#               default=False)
#     adventure = db.Column(db.Boolean,
#               default=False)
#     health = db.Column(db.Boolean,
#               default=False)
#     culture = db.Column(db.Boolean,
#               default=False)
#     backpacking = db.Column(db.Boolean,
#               default=False)
#     digital_nomad = db.Column(db.Boolean,
#               default=False)
   

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





