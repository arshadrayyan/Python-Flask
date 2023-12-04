# First we import flask
from flask import Flask
 
# initialize flask
app = Flask(__name__)
 
# Display first simple welcome msg
@app.route('/')
def msg():
    return '<h1>Welcome From Flask Home</h1> <p> To Enter the Route of /string/yourname</p>'
 
# We defined string  function
@app.route('/string/<name>')
def string(name):
    return "My Name is %s" % name
 
# we run app debugging mode
app.run(debug=True)