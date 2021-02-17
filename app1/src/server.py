'''
References:
    https://stackoverflow.com/a/60441931/13239458
'''

from flask import Flask
from flask_login import LoginManager
import database as db
from web_app import app




# app.add_url_rule('/', view_func=rou.index)
# app.add_url_rule('/login', view_func=rou.login)
# app.add_url_rule('/register', view_func=rou.register)




if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True)

