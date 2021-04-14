from flask import render_template
from app import app
from models.customer_orders import customers

@app.route('/customers')
def index():
    return render_template('index.html', title='Pizza joint', customers=customers)

@app.route('/customers/<id>')
def show(id):
    return render_template('order.html', title='Customer Order', customer=customers[int(id)])