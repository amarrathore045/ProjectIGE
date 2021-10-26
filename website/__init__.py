#This is the python file which automatically runs 
#when the main.py file calls the website folder

from flask import Flask

#This creates the app for our website 
def create_app():
    app = Flask(__name__)
    #Secret key is the value through which our data will be encripted
    #production sites keep their secret key hidden
    app.config['SECRET_KEY']= 'Secret Key Here'

    #These import says that we have other views to import
    from .views import views
    from .auth import auth
    #This will specify which page to show when the page os called
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')

    return app
