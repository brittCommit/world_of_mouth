from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import sys
import cloudinary
import cloudinary.uploader
import cloudinary.api

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
        user_id = user.user_id
        session['user'] = user_id
        return redirect(f'/api/my_travels/{user_id}')

    else:
        flash('Wrong password, try again!')
        return redirect('/login')


@app.route('/register')
def register_new_user():

    return render_template('new_user.html')


@app.route('/new_user', methods=['POST'])
def new_user():
    if request.method == 'POST':
        print('hi')
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    home_country = request.form.get('home_country')
    filename = request.files.get('image-upload')
    if filename:
        response = cloudinary.uploader.upload(filename)
        image = response['secure_url']
    
    user = crud.get_user_by_email(email)
    crud.create_user(email, first_name, user_name, password, home_country, image)

    if user:
        return redirect('/')

    else:   
        user = crud.get_user_by_email(email)
        session['user'] = user.user_id
    print(f'user is {user}')
    return redirect(f'/api/my_travels/{user.user_id}') 


@app.route('/logout')
def logout():
    """Log out a user"""

    del session['user']
    return redirect('/')


@app.route('/create_user')
def create_user():
    """Create a new user"""

    user = crud.create_user(email, first_name, user_name, password, home_country, image)


# ROUTES TO CREATE AND VIEW ROUTES(TRIPS) #


@app.route('/create_route', methods = ['POST'])
def create_route():
    """Create new route"""

    trip_description = request.form.get('trip_description')
    user = crud.get_user_by_id(session['user'])
    route = crud.create_route(user, trip_description)

    return redirect (f'/api/view_stops/{route.route_id}')


@app.route('/view_routes/', methods=['POST','GET'])
def view_routes():
    """View routes based on filter selections"""
    

    stop_dict = {}
    all_routes = []

    #Get form data#
    country = request.form.get('country-code')
    start_city_name = request.form.get('is-start')
    end_city_name = request.form.get('is-end')
    trip_type = request.form.get('trip-type')
    trip_length = request.form.get('trip-length')

    #Queries to handle form data#
    country_routes = crud.get_all_routes_with_stop_with_country_code(country)
    is_start_routes = crud.get_route_id_by_is_start_city_name(start_city_name)
    is_end_routes = crud.get_route_id_by_is_end_city_name(end_city_name)
    
    #Filtering user preferences#
    if len(is_start_routes)>0 and len(is_end_routes)>0:
        for route in is_start_routes:
            if route in is_end_routes:
                all_routes.append(route)

    elif len(is_start_routes)>0 and len(is_end_routes) == 0:
        for route in is_start_routes:
            all_routes.append(route)

    elif len(is_start_routes) == 0 and len(is_end_routes) > 0:
        for route in is_end_routes:
            all_routes.append(route)  

    elif len(is_start_routes) == 0 and len(is_end_routes) == 0:
        for route in country_routes:
            all_routes.append(route)    

    if trip_type != None:
        trip_type_routes = crud.get_routes_by_trip_type(trip_type)
        for route in all_routes:
            if route not in trip_type_routes:
                all_routes.remove(route)

    if trip_length != None:
        trip_length_routes = crud.get_routes_by_trip_length(trip_length)
        print(f'trip length is {trip_length_routes}')
        for route in all_routes:
            if route not in trip_length_routes:
                all_routes.remove(route)

    #package matching routes for html#
    for route in all_routes:
        is_start = crud.get_is_start_by_route_id(route.route_id)
        is_end = crud.get_is_end_by_route_id(route.route_id)
        
        stop_dict[route.route_id] = is_start, is_end

        if len(stop_dict) == 0:
            return alert("No routes found with your search criteria, please modify your filters and try again.")

    return render_template('view_routes.html', stop_dict=stop_dict, all_routes=all_routes)


@app.route('/api/my_travels/<int:user_id>')
def view_routes_by_user(user_id):
    """View routes belonging to a user"""

    user = crud.get_user_by_id(user_id)
    view_routes = crud.get_routes_by_user(user_id)
    favorites = crud.get_favorite_routes_by_user_id(user_id)
    image= user.image
    print(image)

    return render_template('my_travels.html', view_routes = view_routes, user= user,favorites=favorites, image=image)
    

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
    highlights = request.form.get('highlights')

    route_len = crud.get_stops_by_route_id(route_id)
    if len(route_len) == 0:
        is_start = True
    else:
        is_start = False

    route = crud.get_route_by_id(route_id)
    stop = crud.create_stop(city_name, route, stay_length, lat, lng, country_code, is_start, is_end, highlights)
    stop_dict = crud.create_stop_dict(stop)

    return jsonify(stop_dict)

@app.route('/api/view_stops/<int:route_id>')
def route_details(route_id):
    """View route details"""

    route = crud.get_route_by_id(route_id)
    stops = crud.get_stops_by_route_id(route_id)

    print(f' route is {route}')

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

# FAVORITING ROUTES #

@app.route('/api/favorite/<int:route_id>', methods=['POST','GET'])
def favorite_route(route_id):
    """User favorites route"""
 
    user_id = session['user']
    print(f'user id is {user_id}')

    favorite = crud.create_favorite(user_id, route_id)
    print(f'favorite is {favorite}')
    
    return "This trip has been added to your bucket list."


@app.route('/api/unfavorite/<int:route_id>', methods=['POST'])
def unfavorite_route(route_id):
    """User unfavorites route"""

    user_id = session['user']
    favorited_item = crud.get_favorite_id_by_route_and_user_ids(route_id, user_id)

    # del favorited_item = 
    return redirect(request.url)


@app.route('/bucketlist')
def bucketlist():
    """Collection of user's favorited trips"""

    user_id = session['user']
    return get_users_favorites(user_id)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
  