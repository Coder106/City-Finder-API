# schemes.py 
## this script handles the schema for our app with marshmallow & the models module
from flask_marshmallow import Marshmallow 
from models import Client, City

ma = Marshmallow()

class UnitSchema(ma.ModelSchema):
	class Meta:
		model = Client 

unit_schema = UnitSchema()



class CitySchema(ma.ModelSchema):
	class Meta:
		model = City 

city_schema = CitySchema()
cities_schema = CitySchema(many=True)
