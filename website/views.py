#This file stores the standard route for different pages 
#The pages includes home page, etc
#Blueprint spec that the site has bunch of urls to find
from flask import Blueprint ,render_template
#'views' is the name of the variable for our views url
views = Blueprint('views',__name__)

@views.route('/')
#home() function will run whenever the route is called
#here the route is the '/' page 
def home():
    return render_template("prehome.html")
