from flask import Flask, render_template, request, redirect, session, flash
from models.pet import get_all_pets

# insert_pet, get_pet, update_pet, delete_pet
# from models.user import get_user, insert_user, get_all_users, update_user, delete_user
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is not a strong key'

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/')
def index():
    pet_list = get_all_pets()
    return render_template('pet.html', pet_list=pet_list) #user_name = session.get('user_name', 'UNKNOWN'), user_status = session.get('user_status'))


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'GET':
#         return render_template('sign_up_form.html')
    
#     name = request.form.get('name')
#     email = request.form.get('email')
#     password = request.form.get('password')
#     password_hash = generate_password_hash(password)
#     confirm_password = request.form.get('confirm_password')

#     if password != confirm_password:
#         flash('Passwords do not match! Please try again.', 'error')
#         return render_template('sign_up_form.html')
   
#     insert_user(name, email, password_hash)
#     return redirect('login')

# @app.route('/login', methods=['GET', 'POST'])
# def login_user():
#     if request.method == 'GET':
#         return render_template('login_form.html')

#     email = request.form['email']  
#     user = get_user(email)

#     if user is None:
#         flash('Email address or password is incorrect! Please try again', 'error')
#         return redirect('/login')

#     password = request.form['password']
#     password_matches = check_password_hash(user[3], password)

#     if not password_matches:
#         flash('Email address or password is incorrect! Please try again.', 'error')
#         return redirect('/login')

#     else:
#         session['user_id'] = user[0]
#         session['user_name'] = user[1]
#         session['user_email'] = user[2]
#         session['user_status'] = user[4]
#         return redirect('/')

# @app.post('/logout')
# def logout_user():
#     session.pop('user_id')
#     session.pop('user_name')
#     session.pop('user_email')

#     return redirect('/login')