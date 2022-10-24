from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    print("show me the money")
    return render_template("index.html")

# @app.route('/')
# def index():
#     users = User.get_all_users()
#     return render_template('users.html', users=users)

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash("Sorry, you need to login to continue", "error_bad_login")
        return redirect('/index')
    # users = User.get_all_users() #needs to be all recipes created
    return render_template("index.html")

@app.route('/user/register')
def register_new_user():
    print("whats all this then")
    return render_template("register.html")

@app.route('/user/register', methods=['POST'])
def register_user():
    if User.validate_user(request.form) == False:
        return redirect('/register.html')
    user_exists = User.get_email_to_validate(request.form)
    if user_exists != None:
        flash("Sorry! This email already exists. Please enter a new email to register", 'error_user_exists')
        return redirect('/register.html')
    data = {
        **request.form,
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.create(data)
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route("/user/<int:user_id>")
def show_user(user_id): 
    data = {
        "id": user_id
    }
    user = User.show_user(data)
    return render_template("show_user.html", user=user)


@app.route("/user/<int:id>/update", methods=['POST'])
def update_user(id):
    data = {
        "id": id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.update(data)
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def process_login():
    current_user = User.get_email_to_validate(request.form)
    if current_user != None:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Sorry, your email or password is incorrect. Please login or register to continue", "error_no_user")
            return redirect('/index.html')
    session['first_name'] = current_user.first_name
    session['last_name'] = current_user.last_name
    session['email'] = current_user.email
    session['user_id'] = current_user.id
    return redirect('/dashboard')
    
    
# this route just clears the session and effectively logs the user out of this browser
@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')

# @app.route("/user/<int:id>/delete")
# def delete_user(id):
#     data = {
#         "id": id
#     }
#     User.delete(data)
#     return redirect('/')
# @app.route('/user/create', methods=['POST'])
# def create_user():
#     data = {
#         'first_name' : request.form['first_name'],
#         'last_name' : request.form['last_name'],
#         'email' : request.form['email']
#         'password': reqy
#     }
#     User.create(data)
#     return redirect('/user/<int:user_id>')
#     # print("show me the money")