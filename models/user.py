from db import sql_select, sql_write, sql_select_one

def get_all_users():
    users = sql_select('SELECT id, name, email, admin FROM users ORDER BY id ASC;')
    return users

def get_user(email):
    user = sql_select_one("SELECT id, name, email, password_hash, admin FROM users WHERE email = %s;", [email])
    return user

def insert_user(name, email, password_hash):
    sql_write(
        'INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)',
        [name, email, password_hash])

def update_user(id, name, email, password_hash):
    sql_write(
        f"UPDATE users SET name = %s, email = %s, password_hash =%s WHERE id={id}",
        [name, email, password_hash])

def delete_user(id):
    delete_user = sql_write(f"DELETE FROM users WHERE id={id};", [id])
    return delete_user