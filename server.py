from flask import (Flask, render_template, request, flash, session,
                   redirect)
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


@app.route('/login', methods=['POST'])
def login():
    """User login page"""


    email = request.form['email']
    password = request.form['password']

    password_val = crud.get_password_by_email(email)


    if password == password_val:
        session['current_user'] = email
        flash(f'Logged in as {email}')
        return redirect('/view_routes')

    else:
        flash('Wrong password, try again!')
        return redirect('/login')


# @app.route('/register_new_user')
# def new_user():
    
#     first_name = request.form.get('first_name')
#     email = request.form.get('email')
#     password = request.form.get('password')


#     user = crud.get_user_by_email(email)

#     if user:
#         flash('There is already an email with that account. Please try again')

#     else:
#         crud.create_user(email, password)
#         flash('Account created! Please log in.')

#     return redirect('/')

@app.route('/create_user')
def create_user():
    """Create a new user"""

    user = crud.create_user(city_name, route, created_at, 
                    is_start, is_end, stay_length, lat, lng)


@app.route('/create_route')
def create_route():
    """User creates a new trip"""

    route = crud.create_route(city_name, route, created_at, 
            is_start, is_end, stay_length, lat, lng)

@app.route('/view_routes')
def view_routes():
    """View all routes"""

    all_routes = crud.get_routes()

    return render_template ('view_routes.html',
                            all_routes = all_routes)

@app.route('/route_details/<route_id>')
def route_details(route_id):
    """View route details"""

    stops = crud.get_stops_by_route_id(route_id)

    return render_template('view_stops.html', stops=stops)

@app.route('/add_stop')
def add_stop():
    """Add city to trip"""




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
  