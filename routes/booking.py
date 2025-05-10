from flask import Blueprint, request, jsonify, render_template
from models.db import bookings_col
import random

booking = Blueprint('booking', __name__)

def generate_token(student_name):
    first_letter = student_name.strip()[0].upper()
    rand_num = random.randint(1000, 9999)
    return f"{first_letter}-FEE-{rand_num}"

@booking.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        data = request.form
        token = generate_token(data['name'])
        booking_data = {
            "student_name": data['name'],
            "email": data['email'],
            "date": data['date'],
            "time_slot": data['time_slot'],
            "counter": data['counter'],
            "token": token
        }
        bookings_col.insert_one(booking_data)
        return render_template('dashboard.html', token=token)
    return render_template('dashboard.html', token=None)