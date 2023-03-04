from flask import Flask, render_template, request, redirect, session, flash
from models.pet import get_all_pets, insert_pet, get_pet, update_pet, delete_pet
from models.user import get_user, insert_user, get_all_users, update_user, delete_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is not a strong key'

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/')
def index():
    pet_list = get_all_pets()
    return render_template('pet.html', pet_list=pet_list, user_name = session.get('user_name', 'UNKNOWN'), user_status = session.get('user_status'))

@app.route('/create')
def add_pet():
    return render_template("new_pet.html", user_name = session.get('user_name', 'UNKNOWN'))

@app.post('/pet_list')
def create_new_pet():
    insert_pet(
        request.form['image_url'],
        request.form['name'], 
        request.form['type'],
        request.form['breed'],
        request.form['sex'],
        request.form['size'],
        request.form['colour'],
        request.form['age']      
    )
    return redirect('/')

@app.route('/edit_pet', methods=['GET', 'POST'])
def edit_pet():
    if request.method == 'GET':
        id = request.args.get('id')
        item_prefilled = get_pet(id)
        return render_template("edit_pet.html", id=id, item_prefilled=item_prefilled, user_name = session.get('user_name', 'UNKNOWN'))

    id = request.form['id']
    update_pet(
        request.form['id'],
        request.form['image_url'],
        request.form['name'], 
        request.form['type'],
        request.form['breed'],
        request.form['sex'],
        request.form['size'],
        request.form['colour'],
        request.form['age'] 
    )
    return redirect('/')

@app.route('/delete_pet', methods=['GET', 'POST'])
def del_pet():
    if request.method == 'GET':
        id = request.args.get('id')
        item_details = get_pet(id)    
        return render_template("delete_pet.html", id=id, item_details=item_details, user_name = session.get('user_name', 'UNKNOWN'))

    id = request.form['id']
    delete_pet(id)
    return redirect('/')

#######################################################################

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign_up_form.html')
    
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        flash('Passwords do not match! Please try again.', 'error')
        return render_template('sign_up_form.html')
   
    insert_user(name, email, password_hash)
    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login_form.html')

    email = request.form['email']  
    user = get_user(email)

    if user is None:
        flash('Email address or password is incorrect! Please try again', 'error')
        return redirect('/login')

    password = request.form['password']
    password_matches = check_password_hash(user[3], password)

    if not password_matches:
        flash('Email address or password is incorrect! Please try again.', 'error')
        return redirect('/login')

    else:
        session['user_id'] = user[0]
        session['user_name'] = user[1]
        session['user_email'] = user[2]
        session['user_status'] = user[4]
        return redirect('/')

@app.post('/logout')
def logout_user():
    session.pop('user_id')
    session.pop('user_name')
    session.pop('user_email')

    return redirect('/login')

#######################################################################

@app.route('/user_list', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = get_all_users()
        return render_template('users.html', users=users, user_name = session.get('user_name', 'UNKNOWN'))

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        flash('Passwords do not match! Please try again.', 'error')
        return render_template('new_user.html')
   
    insert_user(name, email, password_hash)
    users = get_all_users()
    return render_template('users.html', users=users, user_name = session.get('user_name', 'UNKNOWN'))

@app.route('/add_user')
def add_user():
    return render_template("new_user.html", user_name = session.get('user_name', 'UNKNOWN'))

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():

    id = request.args.get('id')
    email = request.args.get('email')
    user_prefilled = get_user(email)

    if request.method == 'GET':    
        return render_template("edit_user.html", id=id, user_prefilled=user_prefilled, user_name = session.get('user_name', 'UNKNOWN'))

    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        id = request.form['id']
        email = request.form["email"]
        user_prefilled = get_user(email)
        flash('Passwords do not match! Please try again.', 'error')
        return render_template("edit_user.html", id=id, email=email, user_prefilled=user_prefilled, user_name = session.get('user_name', 'UNKNOWN'))

    update_user(
        request.form['id'],
        request.form['name'], 
        request.form["email"],
        request.form['password']
    )
    return redirect('/user_list')

@app.route('/delete_user', methods=['GET', 'POST'])
def del_user():
    if request.method == 'GET':
        id = request.args.get('id')
        email = request.args.get('email')
        user = get_user(email)
        return render_template("delete_user.html", id=id, email=email, user=user, user_name = session.get('user_name', 'UNKNOWN'))

    id = request.form['id']
    delete_user(id)
    return redirect('/user_list')

#######################################################################

@app.route('/contact')
def contact_us():
    return render_template("contact.html", user_name = session.get('user_name', 'UNKNOWN'))