"""CRUD operations"""

from model import db, Country, Route, Stop, connect_to_db

if __name__=='__main__':
    from server import app
    connect_to_db(app)

def create_user(email, user_name, password, home_country):
    """Create and return a new user."""

    user = User(email = email, user_name = user_name, password = password, 
                home_country = home_country)

    db.session.add(user)
    db.session.commmit()

    return user


