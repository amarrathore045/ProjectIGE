#Values to be passed into html pages
value = "Hy there"

#all authorization are done here
from flask import Blueprint,request,flash , redirect ,url_for
from flask.templating import render_template
#'auth' is the name of the variable for our views url
auth = Blueprint('auth',__name__)

#route will be called by the server and the desired output
#for the server is assigned here
#route for Login
@auth.route('/login' , methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
        if len(email) < 4 :
            flash('Email must be grater than 4 charactor.',category='error')
        elif len(password) < 6:
            flash('Password must be atleast 6 charactor.',category='error')
        else:
            pass

    return render_template("login.html", text = value)

@auth.route('/prehome')
def prehome():
    return render_template("prehome.html")


#route for Log-out
@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

