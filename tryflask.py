#this is boilerplate for making a flask app - flask is downloaded previously with the console "sudo pip3 install flask" command

#the below takes the libraries flask and request
from flask import Flask, request, render_template
import os
import datetime
#the right below creates an app based in flask
app = Flask(__name__)

#the below @app conects the html file index.html and renders it
@app.route("/")
def say_hi():
    return render_template("index.html")

#this will make the form send the form input input by the user to be sent to the search page rather than the one that the form is in    
@app.route("/search")
def do_search():
    return "Search Page"

@app.route("/")
def show_photo():
    return "<h1>This is the photos page</h1>"

@app.route("/")
def time():
    now = datetime.datetime.now()
    return "the current time is " + now.strftime("%H:%M:%S")
    
    
#the below ensures that the url has the same string as the <h1> so that when you change the <h1>{0}or {1} the url changes too.    
@app.route("/cars/<car>/image/<carid>")
def cars(car, carid):
    return "<h1>You asked for image {0} for car {1}</h1>".format(carid, car)



#the directly below is is part of the boiler plate for flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

