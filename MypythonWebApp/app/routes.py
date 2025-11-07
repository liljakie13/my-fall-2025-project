"""
This is the routes.py script will contain the routes/path for our application
"""
from flask import Blueprint, render_template, request  ## Blueprint is a way to organize a group of related routes and other code. render_template is used to render html templates
from .db import query_test  ## import the query_test function from the db.py file
from .login import handle_login ## import the login functions from the login.py file
from .register import handle_registration ## import the register functions from the register.py file


bp = Blueprint("main", __name__)  ## create a blueprint object. 'main' is the name of the blueprint, __name__ is the name of the current module

@bp.route("/")  ## this is the route for the home page
def index():
    """
    this is the route for the home page
    """
    
    ok = query_test("SELECT 1")  ## test the database connection
    if ok:
        return "<h1>Flask is running! Database connection is Successful!</h1>"
    else:
        return "<h1>Flask is running! Database test query returned no results!</h1>"
   
## add the route for the login

@bp.route("/login", methods=["GET", "POST"]) ## localhost/login
def login():
    """
    this is the route for the login page
    """
    if request.method == "POST":
       ## login.py script logic here
       print("Hi!")  ## erase this because it just there to prevent error
    return render_template("login.html") ## handle the login form submission
    
@bp.route("/register", methods=["GET", "POST"]) ## localhost/register
def register():
    """
    this is the route for the registration page
    """
    if request.method == "POST":
       ## register.py script logic here
       print("Hi!")  ## erase this because it just there to prevent error
    return render_template("register.html") ## handle the registration form submission  