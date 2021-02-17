

import database as db

def check_database_init():
    
    res = db.list_users()

    print(res)


def login(username, password):

    res = db.user_login(username,password)

    if(res):
        return 1
    return -1


def register(username, password, email):
    
    res = db.user_register(username, password,email)

    return res

def show_users():

    res = db.show_all_users()

    return res