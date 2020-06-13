from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')

# ROUTES TO HANDLE USER LOGIN AND REGISTRATION #

@app.route('/login', methods=['POST'])
def login():
    """User login page"""

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)
    

    if user == None:
        flash(f'Account does not exist for that email')
        return redirect('/new_user')

    elif password == user.password:
        session['current_user'] = email
        flash(f'Logged in as {email}')
        user_id = user.user_id
        return redirect(f'/api/view_routes/{user_id}')

    else:
        flash('Wrong password, try again!')
        return redirect('/')

@app.route('/register')
def register_new_user():

    return render_template('new_user.html')

@app.route('/new_user', methods=['POST'])
def new_user():
    
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    home_country = request.form.get('home_country')

    crud.create_user(email, first_name, user_name, password, home_country)

    print(email)
    return redirect('/view_routes') 

@app.route('/create_user')
def create_user():
    """Create a new user"""

    user = crud.create_user(city_name, route, created_at, 
                    is_start, is_end, stay_length, lat, lng)

# ROUTES TO CREATE AND VIEW ROUTES(TRIPS) #

@app.route('/create_route', methods = ['POST'])
def create_route():
    """Create new route"""

    trip_description = request.form.get('trip_description')
    user = crud.get_user_by_email(session['current_user'])
    route = crud.create_route(user, trip_description)


    return redirect ('/view_routes')

@app.route('/view_routes')
def view_routes():
    """View all routes"""

    all_routes = crud.get_routes()
    return render_template ('view_routes.html',
                            all_routes = all_routes)


@app.route('/api/view_routes/<int:user_id>')
def view_routes_by_user(user_id):
    """View routes belonging to a user"""

    view_routes = crud.get_routes_by_user(user_id)
    print(view_routes)

    return render_template('my_travels.html', view_routes=view_routes)


@app.route('/create_stop')
def create_stop():
    """User creates a new stop"""

    route = crud.create_stop(city_name, route, created_at, 
            is_start, is_end, stay_length, lat, lng)



# ROUTES TO CREATE AND VIEW STOPS #

@app.route('/api/view_stops/<int:route_id>')
def route_details(route_id):
    """View route details"""

    stops = crud.get_stops_by_route_id(route_id)
    return render_template('view_stops.html', stops = stops)

# @app.route('/add_stop')
# def add_stop_to_trip():
#     """Add city to trip"""


# ROUTES FOR HANDLING MAP #

@app.route('/view_map')
def view_map():
    """View map"""
    
    return render_template("homepage.html")

@app.route('/map/<int:route_id>')
def map_by_route_id(route_id):
    """View map by route id"""

#structure to pass into jsonify from flask



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
  