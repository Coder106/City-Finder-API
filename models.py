#models.py
## this is where database model is written , we load the configuration details on the main app.py


from flask import url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin




db = SQLAlchemy()



class Client(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(64), nullable=False)
	api_key = db.Column(db.String(64), unique=True, index=True)


class City(db.Model):
	# id used by db to keep track of which data set is which
	id = db.Column(db.Integer, primary_key=True)
	# Converting ascii to human friendly >> another way of writing the id.index 
	#is set to true to get through the lists much faster.
	slug = db.Column(db.String(64), index=True)
	# city and country are specified as non optional fields
	city = db.Column(db.String(64), nullable=False)
	country = db.Column(db.String(64), nullable=False)

	
	@property
	def url(self):
		return url_for("get_city", id=self.id)



## To create a City object and add it
# city1 = City(slug="Bratislava", city="Bratislava", country="Slovakia")
# db.session.add(city1)

# # To create another city object and add it
#city2 = City(slug="Prague", city="Prague", country="Czech")
# db.session.add(city2)


# # Need to always commit inorder to save changes; Think of GIT :)
# db.session.commit()

# ## To query a City object
# bratislava = City.query.filter(City.slug=="Bratislava").first()
# bratislava.country == "Slovakia"

# ## Updating the Country
# bratislava.Slovakia = "Slovakish"

# # Again updates needs to be commited
# db.session.add(bratislava)
# db.session.commit()




# ## Query to get a City object
# bratislava = City.query.filter_by(slug="bratislava").first()
# bratislava.bratislava = "bratislava"

# # Deleting bratislava
# db.session.delete(bratislava)
# db.session.commit()

# # now bratislava should be gone
# city2 = City.query.filter_by(slug="bratislava").first()
# city2 == None 

# # NB: local variables will be deleted at end of each HTTP request

