# Introduction

## Table of Contents

- [Introduction](#Introduction)
- [Hello World](#HelloWorld)
- [Route](#Route)
- [DynamicRoute](#DynamicRoute)
- [HTTPMethods](#HTTPMethods)
- [GET](#GET)
- [POST](#POST)
- [PUT](#PUT)
- [DELETE](#DELETE)
- [Variable-Rule](#Variable-Rule)
- [String](#String)
- [Integer](#Integer)
- [Float](#Float)
- [URL-Redirection-in-Flask](#URL-Redirection-in-Flask)
- [Simple-Redirect](#Simple-Redirect)
- [url-for()FunctioninFlask](#url-for()FunctioninFlask)
- [RedirectAndErrors](#RedirectAndErrors)
- [ErrorWithAdmin](#ErrorWithAdmin)
- [BadRequestError](#BadRequestError)
- [Forbidden](#Forbidden)
- [StaticFileUses](#StaticFileUses)
- [SendDataFromTemplate](#SendDataFromTemplate)
- [Cookies](#Cookies)


# Introduction
The Tutorial Describes the Basics of the Flask Framework in Python. It designed Basic Flask Applications For Learning.

# HelloWorld

Hello World is the basic application in flask to Print the Hello World on the Screen.

To View Outcome 

Navigate the Project Directory
cd Hello World

Create the Virtual Environment
python -m venv venv

Activate the Environment on Windows
.\venv\Scripts\activate

Install the Flask FrameWork
pip install flask

Execution Process
Navigate to the cd Hello World/App

.\app.py on the Terminal.

# Route

Route is The Basic Routing using Flask Application.
Using the Specified the Route Parameter as (/hello).

For Outcome follow the Steps mentioned Above, After the Below Directory.

Navigate the Project Directory
cd Route

# DynamicRoute

Dynamic Route is used to Route the Page and it's Information Based on the Specified User like (/user/<UserName>).

For Outcome follow the Steps mentioned Above, After the Below Directory.

Navigate the Project Directory
cd Dynamic Route

# HTTPMethods

we will learn how to handle HTTP methods, such as GET and POST in Flask using Python. Here, we will understand the concept of HTTP, GET, and HTTP POST, and then we will the example and implement each in Flask. Before starting let’s understand the basic terminology:

# GET

GET: to request data from the server.

To Request the Page Using GET Method in Python Flask.

For Outcome follow the Steps After the Below Directory.

Navigate the Project Directory
cd HTTP Methods\GET

Create the Virtual Environment inside it.
python -m venv venv

navigate to the Environment Directory using
.\venv\Scripts\activate

Install the Flask FrameWork
pip install flask

To Run the Application Using
.\app\app.py

# POST

POST: to submit data to be processed to the server.

To Request the Page Using POST Method in Python Flask.

For Outcome follow the Steps After the Below Directory.

Navigate the Project Directory
cd HTTP Methods\POST

Create the Virtual Environment inside it.
python -m venv venv

navigate to the Environment Directory using
.\venv\Scripts\activate

Install the Flask FrameWork
pip install flask

To Run the Application Using
.\app\app.py

# PUT

PUT: A PUT request is used to modify the data on the server. It replaces the entire content at a particular location with data that is passed in the body payload. If there are no resources that match the request, it will generate one.

To Request the Page Using PUT Method in Python Flask.

For Outcome follow the Steps After the Below Directory.

Navigate the Project Directory
cd HTTP Methods\PUT

Create the Virtual Environment inside it.
python -m venv venv

navigate to the Environment Directory using
.\venv\Scripts\activate

Install the Flask FrameWork
pip install flask

To Run the Application Using
.\app\app.py

To See the Value Changes Refresh Once the Data is Submitted By HTML Form.

# DELETE

DELETE: A DELETE request is used to delete the data on the server at a specified location.

To Request the Page Using DELETE Method in Python Flask.

For Outcome follow the Steps After the Below Directory.

Navigate the Project Directory
cd HTTP Methods\DELETE

Create the Virtual Environment inside it.
python -m venv venv

navigate to the Environment Directory using
.\venv\Scripts\activate

Install the Flask FrameWork
pip install flask

To Run the Application Using
.\app\app.py

# Variable-Rule

The Variable-Rule Defines the DataType Specified by the Dynamic URL's on the Flask Framework.

# String

The String Variable Represents the Type of the URL Should be on Letters normally

Enter the Navigation string/yourname to see the magic route.

# Integer

The Integer Variable Represents the Type of the URL Should be on Numbers only.

Enter the Navigation integer/yourage to see the magic route.

# Float

The Float Variable Represents the Type of the URL Should be on Decimal Points

Enter the Navigation string/yourvalletbalance in float to see the magic route.


# URL-Redirection-in-Flask

Redirect the Home Page By URL in Flask.

# Simple-Redirect

Redirect the (/) Route to the (/helloworld) from the Home Page in Flask.

# url-for()FunctioninFlask

Redirect the (/) Route to the (/admin) Or (/user/username) to view the Result or else click the Link from Home Page.

# RedirectAndErrors

The URL Redirects Using the "Redirect" Class From Flask based on the Method POST or GET.

# ErrorWithAdmin

The ErrorsWithAdmin is to Check Weather the User Enters the Username as the "Admin" then Sucess 
Message will Show Otherwise the Default Route will Work.

# BadRequestError

The Error message will display when the User Enters the name with numbers it will Display the Following Error. (Error Code 400).

# Forbidden

The Error message will display when the User Enters the name with numbers it will Display the Following Error. (Error Code 403).

# StaticFileUses

The Program contains the Static Folder in it's app directory to understand the JavaScript and CSS files how it is calling through the Flask Framework.

# SendDataFromTemplate

Send the data from the HTML Form data to Template in the Table Format.

# Cookies

the Cookies is used to add the Entered in the Fields to remember the user,Here we Described the Feature in the flask.