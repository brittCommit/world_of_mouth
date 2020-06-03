from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Country(db.Model):
    """A country."""

    __tablename__ = 'countries'

    country_id = db.Column(db.String,
                        primary_key = True)
    country_name = db.Column(db.String, 
                        nullable = False)

    route = db.relationship('Route')

    def __repr__(self):
        return f'<Country is {self.country_name} with id {self.country_id}>'


class Route(db.Model):
    """A route"""

    __tablename__ = 'routes'

    route_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    country_id = db.Column(db.String, 
                        db.ForeignKey('countries.country_id'))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    is_completed = db.Column(db.Boolean, 
                        default = False)

    stop = db.relationship('Stop')
    country = db.relationship('Country')
    user = db.relationship('User')
 
    def __repr__(self):
        return f"""<Route id is {self.route_id} in country id {self.country_id}
                by user {self.user_id} and the trip is completed {self.is_completed}>"""


class Stop(db.Model):
    """A stop"""

    __tablename__ = 'stops'

    stop_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement =True)
    city_name = db.Column(db.String, 
                        nullable = False,)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    created_at = db.Column(db.DateTime, 
                        default = datetime.utcnow)
    is_start = db.Column(db.Boolean, 
                        default = False)
    is_end = db.Column(db.Boolean, 
                        default = False)
    stay_length = db.Column(db.Integer)

    route = db.relationship('Route')

    def __repr__(self):
        return f"""<Stop #{self.stop_id} in {self.city_name} on route #{self.route_id}>"""


class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement =True)
    email = db.Column(db.String,
                        nullable = False)
    user_name = db.Column(db.String,
                        nullable = False)
    password = db.Column(db.String,
                        nullable = False)
    traveler_type = db.Column(db.String)
    language = db.Column(db.String)
    home_country = db.Column(db.String)

    route = db.relationship('Route')

    def __repr__(self):
        return f"""<User id #{self.user_id} belongs to {self.email}, {self.user_name}
                and is from {self.home_country}>"""


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
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







