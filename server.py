from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
# from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/login')
def login():
    """User login page"""



@app.route('/create_user')
def create_user():
    """Create a new user"""

    user = crud.create_user(city_name, route, created_at, 
                    is_start, is_end, stay_length, lat, lng)


@app.route('/create_route')
def create_route():
    """User creates a new trip"""

    route = (crud.create_routecity_name, route, created_at, 
            is_start, is_end, stay_length, lat, lng)


@app.route('/add_stop')
def add_stop():
    """Add city to trip"""




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)