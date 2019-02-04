#app.py
### 
''' This the main API file ,it covers following services:
	*Given a European City  on the request payload, API returns the City name mapped to Country name.
	'''
import sys
from flask import Flask, jsonify, url_for,request
from flask_login import LoginManager, current_user, login_required
from models import db,Client, City
from schemes import ma, city_schema, cities_schema 
from slugify import slugify




# Inititate the loging manager class instance
login_manager = LoginManager()


# Define app class & initiate the database connection
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cities.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
ma.init_app(app)
login_manager.init_app(app) 



## login manager 
@login_manager.user_loader
def load_unit(unit_id):
	return Unit.get(unit_id)


# loading request to check the api key
@login_manager.request_loader
def load_city_from_request(request):
	api_key = request.headers.get('Authorization')
	if not api_key:
		return None 
	return Unit.query.filter_by(api_key=api_key).first()


@app.route("/whoami")
def which_unit():
    if current_user.is_authenticated:
        unit_name = current_user.unit_name 
    else:
        unit_name = "incognito"
    return jsonify({"name": unit_name})	


@app.route("/profile")
@login_required
def unit_profile():
	return unit_schema.jsonify(current_user)



## Retrieve all CITIES >> request to be sent if you need to view all Entries!
@app.route("/city_mapper/", methods=["GET"])
def show_all_cities():
    all_cities = City.query.all()
    return cities_schema.jsonify(all_cities)



# CITY Read method >> read the client CITY request reply with output(CITY, COUNTRY pair)
@app.route("/city_mapper/read/<slug>")
def get_city(slug):
	city = City.query.filter(City.slug==slug).first_or_404() 
	output = {
	"City": city.city,
	"Country": city.country,
	}
	
	return jsonify(output)


# CITY Create method >> Receive updates on entries and reply with success message
@app.route("/city_mapper/create/", methods=["POST"])
def create_city():
	city, errors = city_schema.load(request.form)
	if errors:
		resp = jsonify(errors)
		resp.status_code = 400
		return resp 
	city.slug = slugify(city.city)
	db.session.add(city)
	db.session.commit()

	# return with HTTP response code
	resp = jsonify({"message": "created"})
	resp.status_code = 201
	resp.headers["Location"] = city.url
	return resp 




## CITY ,COUNTRY UPDATE method
@app.route("/city_mapper/update/", methods=["PUT"])
def update_city():
	city = request.form.get("city")
	if not city:
		return "City required", 400
	country = request.form.get("country")
	if not country:
		return "Country required", 400

	slug = city

	# Update resource in the database
	city = City(slug=slug, city=city, country=country)
	db.session.add(city)
	db.session.commit()

	# return with HTTP response code
	resp = jsonify({"message": "Updated"})
	resp.status_code = 201
	location = url_for("update_city", slug=slug)
	resp.headers["Location"] = location 
	return resp 


## CITY,COUNTRY > DELETE resource method
@app.route("/city_mapper/delete/<slug>", methods=["DELETE"])
def delete_city(slug):

	city = City.query.filter(City.slug==slug).first_or_404() 
	db.session.delete(city)
	db.session.commit()
	return jsonify({"message": "Entry Deleted!"})




# # Error handler,>> custom Error handler
@app.errorhandler(404)
def resource_not_found(e):
	resp = jsonify({"error": "Resource/Country Not Found"})
	return resp 


@app.errorhandler(401)
def unauthorized(error):
	resp = jsonify({"error": "unauthorized"})
	resp.status_code = 401
	return resp



## main section for the app to run >> create database with sample entry (seed data to database)
if __name__=="__main__":
	if "createdb" in sys.argv:
		with app.app_context():
			db.create_all()
		print("Datbase created!")
	elif "seeddb" in sys.argv:
		with app.app_context():
			city1 = City(slug="Bratislava", city="Bratislava", country="Slovakia")
			db.session.add(city1)
			db.session.commit()
			city2 = City(slug="Vienna", city="Vienna", country="Austria")
			db.session.add(city2)
			db.session.commit()
			city3 = City(slug="Budapest", city="Budapest", country="Hungary")
			db.session.add(city3)
			db.session.commit()
			city4 = City(slug="Stockholm", city="Stockholm", country="Sweden")
			db.session.add(city4)
			db.session.commit()
			city5 = City(slug="Paris", city="Paris", country="France")
			db.session.add(city5)
			db.session.commit()
			city6 = City(slug="Oslo", city="Oslo", country="Norway")
			db.session.add(city6)
			db.session.commit()
			city7 = City(slug="Amsterdam", city="Amsterdam", country="Netherlands")
			db.session.add(city7)
			db.session.commit()
			city8 = City(slug="Bern", city="Bern", country="Switzerland")
			db.session.add(city8)
			db.session.commit()
			city9 = City(slug="Brussels ", city="Brussels ", country="Belgium")
			db.session.add(city9)
			db.session.commit()
		print("Datbase seeded!")
	else:
		app.run(host='127.0.0.1', debug=True, port='8000')
