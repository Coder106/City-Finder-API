              README ->FOR TEACHING PURPOSES

This Demo Web API Service is created using Flask framework. It is super easy to use(coming from Python :)), which will provide the basic components of a modern framework like supporting database interface extensions, JSON data validation, out of the box development web server...

Here are the modules needed(The modules list can also be found on the requirements.txt file):
###### 
 Flask,
 Flask-SQLAlchemy,
 Flask-Marshmallow,
 Marshmallow-SQLAlchemy,
 Flask-Login,
 python-slugify
###### 

The steps after extracting the files:
    1. In app.py module modify per need the ip address and port number you would like to run the server at:
        "app.run(host='127.0.0.1', port='8000', debug=True)"
    2. If you are running the web server in development mode run the command
    "python app.py" , if a 'hot-reload' is needed you can set the 'debug=True'  inside the app.run(), that enables the app to pick the code update without re-starting web server manually. 
    OR For Development :
    -Run "gunicorn -w 4 -b 127.0.0.1:8000 app:app"  the first app represents your application module name and the second is set to app by default.Since our application's main module is app we can use the command as it is.
    3. To stop web server you can use CTRL + C for development mode OR for production we could use nginx combined with gunicorn & supervisor to manage the start,stop and restart the server.That is all from web server side.easy right?

After running the server go to http://127.0.0.1:8000/city_mapper/read/ in your browser.It should respond with {"status": "failure", "message": "Invalid request"} since the it's expecting a JSON payload .

In order to POST request with JSON content you can use a script which is used for testing  API functionality (we just need to update the path and parameter or any other script or tool like cURL or Postman-> we can use currently quite a number of paths ->>> 1.  "http://127.00.1:7779/city_mapper/read/Bratislava", If you need to view all the entries you can use the path http://127.0.0.1:8000/city_mapper/ . using GET requests and for POST request we could use 
http://127.0.0.1:8000/city_mapper/update and etc. Need to  define our JSON payload which by the minimum need to contain the CITY name and COUNTRY Name. We can make custom script using any language perl,python  or we can use cURL which is very easy to use and command line friendly.

-All CRUD Operations are supported Create , Read, Update and Delete are written in the main app as routes.



Samson Takele Demma
Tel +421-949-227-950

