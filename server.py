from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

import cloudinary
import cloudinary.uploader
import cloudinary.api

from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

cloud_name = os.environ["cloud_name"]
cloudinary_api_key = os.environ["cloudinary_api_key"]
cloudinary_api_secret = os.environ["cloudinary_api_secret"]

cloudinary.config(
    cloud_name = cloud_name,
    api_key = cloudinary_api_key,
    api_secret = cloudinary_api_secret)

@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


# ROUTES TO HANDLE USER LOGIN/LOGOUT AND REGISTRATION #

@app.route('/user_login')
def route_to_login():

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """User login page"""

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)
    
    if user == None:
        flash(f'Account does not exist for that email, please try again or create a new account.')
        return redirect('/login')

    elif password == user.password:
        session['current_user'] = email
        flash(f'Logged in as {email}')
        user_id = user.user_id
        return redirect(f'/api/view_routes/{user_id}')

    else:
        flash('Wrong password, try again!')
        return redirect('/login')


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
    filename = request.files.get("image-upload")
    print(f'filename is {filename}')
    if filename:
        response = cloudinary.uploader.upload(filename)
        print(f'filename is {filename}')
    image = secure_filename(filename.filename)
    print(f'image is {image}')
    user = crud.get_user_by_email(email)

    crud.create_user(email, first_name, user_name, password, home_country, image)

    email = request.form['email']
    user = crud.get_user_by_email(email)

    print(email)
    return redirect(f'/api/view_routes/{user.user_id}') 


@app.route('/logout')
def logout():
    """Log out a user"""

    error = None
    if "user" in session:
        user = session ['user']
    session.pop('user', None)
    flash('You have been logged out!', 'info')
    return render_template ('homepage.html', error = error)


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

    return redirect (f'/api/view_stops/{route.route_id}')


@app.route('/view_routes/<country>')
def view_routes(country):
    """View all routes"""


    all_routes = crud.get_all_routes_with_stop_with_country_code(country)
    stop_dict = {}

    for route in all_routes:
        is_start = crud.get_is_start_by_route_id(route.route_id)
        print(f'a route is {route}')
        is_end = crud.get_is_end_by_route_id(route.route_id)
        
        # if len(is_end) == 0:
        #     stop_dict[route.route_id] = is_start

        
        stop_dict[route.route_id] = is_start, is_end

    
    return render_template('view_routes.html', all_routes = all_routes, stop_dict=stop_dict)


@app.route('/api/view_routes/<int:user_id>')
def view_routes_by_user(user_id):
    """View routes belonging to a user"""

    user = crud.get_user_by_id(user_id)
    view_routes = crud.get_routes_by_user(user_id)
    print(view_routes)

    return render_template('my_travels.html', view_routes = view_routes, user= user)
    

# ROUTES TO CREATE AND VIEW STOPS #


@app.route('/create_stop', methods = ['POST'])
def create_stop():
    """User creates a new stop"""

    city_name = request.form.get('city-name') 
    route_id = request.form.get('route-id')
    stay_length = request.form.get('stay-length')
    lat = request.form.get('lat')
    lng = request.form.get('lng')
    country_code = request.form.get('country-code')
    is_end = request.form.get('is-end')
    is_end = bool(is_end)

    route_len = crud.get_stops_by_route_id(route_id)
    if len(route_len) == 0:
        is_start = True
    else:
        is_start = False

    route = crud.get_route_by_id(route_id)
    stop = crud.create_stop(city_name, route, stay_length, lat, lng, country_code, is_start, is_end)
    stop_dict = crud.create_stop_dict(stop)

    return jsonify(stop_dict)

@app.route('/api/view_stops/<int:route_id>')
def route_details(route_id):
    """View route details"""

    route = crud.get_route_by_id(route_id)
    stops = crud.get_stops_by_route_id(route_id)

    return render_template('view_stops.html', stops = stops,
                                              route_id = route_id,
                                              route = route)


# ROUTES FOR HANDLING MAP #


@app.route('/view_map')
def view_map():
    """View map"""
    
    return render_template("homepage.html")

@app.route('/api/map/<int:route_id>', methods = ['POST','GET'])
def map_by_route_id(route_id):
    """View map by route id"""

    stops = [
            {"stop_id": stop.stop_id,
            "city_name": stop.city_name,
            "route_id": stop.route_id,
            "stay_length": stop.stay_length,
            "lat": stop.lat,
            "lng":stop.lng
            }
            for stop in crud.get_stops_by_route_id(route_id)
    ]

    print(stops)

    return jsonify(stops)

# @app.route('/api/map/<str:country_code>')
# def map_by_country_code(country_code):
#     """View map by country_code"""

#     routes = [
#             {"stop_id": stop.stop_id,
#             "city_name": stop.city_name,
#             "route_id": stop.route_id,
#             "stay_length": stop.stay_length,
#             "lat": stop.lat,
#             "lng":stop.lng
#             }
#             for route in crud.get_stops_by_route_id(route_id)
#     ]

#     print(routes)

#     return jsonify(routes)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
  