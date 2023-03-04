from db import sql_select, sql_write, sql_select_one

def get_user(email):
    user = sql_select_one("SELECT id, name, email, password_hash, admin FROM users WHERE email = %s;", [email])
    return user

def insert_user(name, email, password_hash):
    sql_write(
        'INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)',
        [name, email, password_hash])