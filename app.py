#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#mongo
app.config["MONGO_URI"] = "mongodb://192.168.56.50:27017/temperature" # Connect to the mongo instance running on the node-red server
mongo = PyMongo(app)

# Route for the default or index page for the app. Routes to index.html
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# The next three routes are for api calls made the the flask server. Will return various temperature data based on the api called
@app.route("/get_one_temp_api")
def temp1():
    one_temp = mongo.db.temperature.find_one()
    #print(temp_reading)
    return str(one_temp)

@app.route("/get_ten_temps_api") # Gets 10 temperature readings from mongo, displayed in a JSON format
def temp10():
    temps = ""
    ten_temps = mongo.db.temperature.find().limit(10)
    for temp in ten_temps:
        temps=temps+str(temp)
        print(temps)
    return temps

@app.route("/recent_temps")
def recent():
    temps = mongo.db.temperature.find().limit(10)
    
    return render_template('temps.html',temps=temps)

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyonepy