"""a database"""

import os
import json
from random import choice, randint 
from datetime import datetime

import crud 
import server 
import model
from model import User, Route, Stop, TripType, RouteType, Favorite

os.system('dropdb routes')
os.system('createdb routes')

model.connect_to_db(server.app)
model.db.create_all()


def seed_users():
  """Create users to seed db"""

  with open('data/users.json') as f:
      user_data=json.loads(f.read())

  for user in user_data:
      email = user['email']
      first_name = user['first_name']
      user_name = user['user_name']
      password = user['password']
      home_country = user['home_country']
      image = user['image']                                         
                                                                                    
      db_user = crud.create_user(email, 
                                 first_name,
                                 user_name,
                                 password,
                                 home_country,
                                 image)


def seed_routes():
  """Create routes to seed db"""

  seed_users()

  with open('data/routes.json') as f:
    route_data=json.loads(f.read())

  for route in route_data:
      user_id = route['user_id']
      is_completed = route['is_completed']
      trip_description = route['trip_description']

      user = crud.get_user_by_id(user_id)
      crud.create_route(user,trip_description)


def seed_stops():
  """Create stops to seed db"""

  seed_routes()

  with open('data/stops.json') as f:
    stop_data=json.loads(f.read()) 

  for stop in stop_data:
      city_name = stop['city_name']
      route_id = stop['route_id']
      is_start = stop['is_start']
      is_end = stop['is_end']
      stay_length = stop['stay_length']
      lat = stop['lat']
      lng = stop['lng']
      country_code = stop['country_code']
      highlights = stop['highlights']

      created_at = datetime.strptime(stop['created_at'], '%Y-%m-%d')
      route = crud.get_route_by_id(route_id)
      crud.create_stop(city_name, route, stay_length, lat, lng, country_code, is_start, is_end, highlights)

def seed_trip_types():
  """Create trip types to seed db"""
  
  seed_stops()

  with open('data/tripTypes.json') as f:
      trip_data=json.loads(f.read()) 

  for trip in trip_data:
      trip_type = trip['trip_type']

      crud.create_trip_type(trip_type)

def seed_route_types():
  """Create trip types to seed db"""
  
  seed_trip_types()

  with open('data/routeTypes.json') as f:
      route_data=json.loads(f.read()) 

  for route in route_data:
      route_id = route['route_id']
      trip_type_id  = route['trip_type_id']

      crud.create_route_type(route_id, trip_type_id)

def seed_favorites():
  """Create favorites to seed db"""

  seed_route_types()

  with open('data/favorites.json') as f:
    favorites=json.loads(f.read())

    for favorite in favorites:
      user_id = favorite['user_id']
      route_id = favorite['route_id']

      crud.create_favorite(user_id,route_id)

seed_favorites()


print("Database successfully seeded!")








    
