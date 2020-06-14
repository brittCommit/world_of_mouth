"""a database"""

import os
import json
from random import choice, randint 
from datetime import datetime

import crud 
import server 
import model
from model import User, Route, Stop

os.system('dropdb routes')
os.system('createdb routes')

model.connect_to_db(server.app)
model.db.create_all()



def seed_users():
  """Create users to seed db"""

  with open('data/users.json') as f:
      user_data=json.loads(f.read())

  for user in user_data:
      email, first_name, user_name, password, home_country = (user['email'], 
                                               user['first_name'], 
                                               user['user_name'],
                                               user['password'],
                                               user['home_country'])   
      db_user = crud.create_user(email, 
                                 first_name,
                                 user_name,
                                 password,
                                 home_country)


def seed_routes():
  """Create routes to seed db"""

  seed_users()

  with open('data/routes.json') as f:
    route_data=json.loads(f.read())

  for route in route_data:
      user_id, is_completed, trip_description = (route['user_id'],
                               route['is_completed'],
                               route['trip_description'])

      user = crud.get_user_by_id(user_id)
      crud.create_route(user, is_completed,trip_description)


def seed_stops():
  """Create stops to seed db"""

  seed_routes()

  with open('data/stops.json') as f:
    stop_data=json.loads(f.read()) 

  for stop in stop_data:
      city_name, route_id, is_start, is_end, stay_length, lat, lng = (stop['city_name'],
                               stop['route_id'],
                               stop['is_start'],
                               stop['is_end'],
                               stop['stay_length'],
                               stop['lat'],
                               stop['lng'])

      created_at = datetime.strptime(stop['created_at'], '%Y-%m-%d')

      route = crud.get_route_by_id(route_id)
      crud.create_stop(city_name, route, stay_length, lat, lng)

  print("Database successfully seeded!")






    
