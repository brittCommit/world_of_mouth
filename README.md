# World of Mouth

>World of Mouth brings the travel community together by creating a hub where travelers can share and save their trip details. Fellow travelers can view trips, get insights and inspiration for their own adventures. The idea for this app was born during Britt's 5 month backpacking trip as a way to make planning travel simpler.

### Technologies
  - Tech Stack: Python, JavaScript, HTML, CSS, Flask, Jinja, jQuery, AJAX, PostgreSQL, SQLAlchemy, Bootstrap
  - APIs: Google Places API,  Google Maps JavaScript API,  Cloudinary API
### Features
  - Create trips and cities with stay details
  - Search other users trips by country
  - Advanced filtering by first and/or last city, trip length and trip type
  - Display trip markers on hover
  - Add trips to bucket list
  - Registration, Login, Logout
  
#### Search and results
![countrySearch](https://github.com/b-hutt/world_of_mouth/blob/master/static/img/countrySearch.gif)
#### View itinerary
![itinerary](https://github.com/b-hutt/world_of_mouth/blob/master/static/img/itinerary.gif)
#### Create a new trip
![newTrip](https://github.com/b-hutt/world_of_mouth/blob/master/static/img/newTrip.gif)




### Installation
#### Prerequisites
  - API keys for Google Places,  Google Maps JavaScript and  Cloudinary
  - Python3
  - PostgreSQL

### Let's go! ✈
#### Clone or fork repository
```sh
$ git clone https://github.com/b-hutt/world_of_mouth.git
```
#### Create and activate a virtual environment inside your WOM directory
```sh
$ virtualenv
$ source env/bin/activate
```
#### Install requirements
```sh
$ pip3 install -r requirements.txt
```

Add your google api key to the 3 html files(homepage, view_stops and view_routes).
Add your cloudinary api key, secret and cloud information to the cloudinary.config section on server.py

#### Create database
```sh
$ createdb routes
```
#### Seed database
```sh
$ python3 seed_database.py
```
#### Start your server
```sh
$ python3 server.py
```

### About the Engineer

Prior to attending Hackbright Academy’s 12-week immersive full-stack software engineering program, Britt received a B.S.in Economics and an MBA from the University of Nevada. She has held a variety of logistics facing roles in companies across various industries, from auto manufacturing to e-commerce. Most notably she was an SME and a Project Manager for a global ERP implementation — during this time it became apparent that she enjoyed being part of a team that designed and implemented technical solutions. 

She decided to pursue software engineering so she could put her strengths of ideation and problem solving to use and further pursue roles in which she can help create products that provide solutions and have positive impacts. In her free time, she enjoys traveling, hiking, yoga and volunteering for Urban Lotus Project.

### Acknowledgments

Thank you to my mentors, classmates and advisors who provided direction, support, ideas and endless hours of debugging to help make this project come alive. 🙏




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [countrySearch]: <https://github.com/b-hutt/world_of_mouth/blob/master/static/img/countrySearch.gif>
   [newTrip]: <https://github.com/b-hutt/world_of_mouth/blob/master/static/img/newTrip.gif>
   [itinerary]: <https://github.com/b-hutt/world_of_mouth/blob/master/static/img/itinerary.gif>
