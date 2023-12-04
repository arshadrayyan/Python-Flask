

# first we import flask
from flask import Flask
 
# Initialize flask function
app = Flask(__name__)
 
@app.route('/')
def msg():
    return '<h1>Welcome From Flask Home</h1> <p> To Enter the Route of /float/accountbalancefloat</p>'
 
# define float function
@app.route('/float/<float:balance>')
def vfloat(balance):
    return "My Account Balance %f" % balance
 
 # we run our code in debugging mode
app.run(debug=True)