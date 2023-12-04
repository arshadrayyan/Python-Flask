# first we import flask
from flask import Flask
 
# Initialize flask function
app = Flask(__name__)
 
@app.route('/')
def msg():
    return '<h1>Welcome to The Flask Home Page</h1> <p>To Enter the Route with \integer\yourage</p>'
 
# define int function
@app.route('/integer/<int:age>')
def vint(age):
    return "I am %d years old " % age
 
# we run our code in debug mode
app.run(debug=True)