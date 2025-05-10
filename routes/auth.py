from flask import Blueprint, request, render_template, redirect
from models.db import students_col

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form

        # Check if student already exists
        if students_col.find_one({'email': data['email']}):
            return "Student already exists. Please login."

        # Register new student
        students_col.insert_one({
            "name": data['name'],
            "email": data['email'],
            "password": data['password']
        })

        return redirect('/login')  # After successful registration

    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form

        # Find student with matching credentials
        student = students_col.find_one({
            "email": data['email'],
            "password": data['password']
        })

        if student:
            return redirect('/dashboard')  # After successful login

        return "Invalid credentials. Please try again."

    return render_template('login.html')
