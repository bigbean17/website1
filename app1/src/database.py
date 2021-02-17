import sqlite3


#####################################

# don't forget to close cur and conn after doing the action


#####################################

def close_conn_cur(conn, cur):
    cur.close()
    conn.close()
    

def connect_db():
    
    conn = sqlite3.connect("webApp.db")
    cur = conn.cursor()

    return cur, conn


def init_db():
    init_user()
    init_message()



def list_users():
    cur,conn = connect_db()
    
    query = '''SELECT username FROM USER'''

    cur.execute(query)
    res = cur.fetchall()
    close_conn_cur(conn,cur)
    return res


def user_login(username, password):

    cur,conn = connect_db()
    query = "SELECT * FROM USER WHERE username = ? AND password = ?"
    params = (username,password)

    cur.execute(query, params)
    res = cur.fetchone()
    close_conn_cur(conn,cur)
    return res

def user_register(username, password, email):

    cur,conn = connect_db()

    query = "SELECT * FROM USER WHERE username = ?"
    params = (username,)

    cur.execute(query, params)
    res = cur.fetchone()
    
    if(res):
        close_conn_cur(conn,cur)
        # user already exists, tell model
        return -1

    #TODO: Need to check if the name is legal, don't contain special characters!
    #TODO: Need to check if the password is safe  (length, complexity)
    
    else:
        
        # legal name, no repetation
        store_info = "INSERT INTO USER VALUES(null,?,?,?,0,0)"
        params=(username, password, email)

        cur.execute(store_info,params)
        conn.commit()
        show_all_users()
        close_conn_cur(conn,cur)
        return 1

def show_all_users():

    cur, conn = connect_db()
    query = "SELECT username FROM USER"

    cur.execute(query)
    res = cur.fetchall()


    return res



def init_user():
    cur,conn = connect_db()

    query = '''

        DROP TABLE IF EXISTS USER;

        CREATE TABLE USER(

            uid int primary key,
            username varchar(50),
            password varchar(50),
            email varchar(50),
            is_admin int,
            is_banned int

        );

    '''

    cur.executescript(query)
    conn.commit()

    query = '''insert into user values (0,'admin_user_n_0','n0_user_password','admin_email@admin.com', 1, 0);'''
    cur.execute(query)
    close_conn_cur(cur,conn)


def init_message():

    query = '''

        DROP TABLE IF EXISTS Message;

        CREATE TABLE Message(

            mid int primary key,
            username varchar(50),
            content varchar (500)
        );
    '''

    cur.executescript(query)
    conn.commit()

    query = '''INSERT INTO Message values (0, admin, 'welcome to our forum, lets chat!')'''
    cur.execute(query)
    close_conn_cur(cur,conn)

