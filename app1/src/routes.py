from flask import render_template, redirect, flash, url_for, abort, request
from flask_login import current_user, login_user, logout_user, login_required
from flask import Flask
import model as mod
from web_app import app



@app.route('/')
def index():
    mod.check_database_init()
    return render_template("index.html")

@app.route('/login',methods=['POST','GET'])
def login():
    
    if(request.method == 'POST'):
        name = request.form['username']
        password = request.form['password']

        if(mod.login(name,password) == 1):
            return "correct"
        else:
            return "incorrect"

        
    else:
        return render_template("login.html")


@app.route('/register', methods=['GET','POST'])
def register():
    if(request.method == "POST"):

        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        res = mod.register(name,password,email)
        if(res == -1):
            return "name repeted!"
        elif(res == 0):
            return "illegal name or password!"
        else:
            return "successful register!"

    return render_template("register.html")


@app.route('/show_users',methods=["GET"])
def show_all_users():

    #TODO:  this is used to test the register function, make this function only visable to admin!
    res = mod.show_users()
    return render_template("all_users.html",res = res)


@app.route("/forum", methods=["POST","GET"])
def forum():

    pass
