import os
import sys

from flask import * #importing flask (Install it using python -m pip install flask)


app = Flask(__name__) #initialising flask


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")
def home():
    return render_template("home.html") #rendering our home.html contained within /templates

@app.route("/actions") #defining the routes for the actions funtion
def actions():
    return render_template("actions.html") #rendering our actions.html contained within /templates

@app.route("/read") #defining the routes for the actions funtion
def read():
    return render_template("read.html") #rendering our actions.html contained within /templates

@app.route("/play") #defining the routes for the actions funtion
def play():
    return render_template("play.html") #rendering our actions.html contained within /templates

if __name__ == "__main__":
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)
