from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Basic Flight Delay Insurance', 'description': 'Get compensated for delays over 2 hours.', 'image': 'https://via.placeholder.com/150'},
    {'id': 2, 'name': 'Premium Flight Delay Insurance', 'description': 'Get compensated for delays over 1 hour and additional perks.', 'image': 'https://via.placeholder.com/150'},
    {'id': 3, 'name': 'Ultimate Flight Delay Insurance', 'description': 'Get compensated for any delay and enjoy VIP lounge access.', 'image': 'https://via.placeholder.com/150'},
    {'id': 4, 'name': 'Economy Flight Delay Insurance', 'description': 'Affordable coverage for delays over 3 hours.', 'image': 'https://via.placeholder.com/150'},
    {'id': 5, 'name': 'Business Class Delay Insurance', 'description': 'Premium coverage for business travelers.', 'image': 'https://via.placeholder.com/150'},
    {'id': 6, 'name': 'First Class Delay Insurance', 'description': 'Comprehensive coverage for first class passengers.', 'image': 'https://via.placeholder.com/150'},
    {'id': 7, 'name': 'Family Flight Delay Insurance', 'description': 'Coverage for the whole family.', 'image': 'https://via.placeholder.com/150'},
    {'id': 8, 'name': 'Group Flight Delay Insurance', 'description': 'Special rates for groups of 10 or more.', 'image': 'https://via.placeholder.com/150'},
    {'id': 9, 'name': 'Corporate Flight Delay Insurance', 'description': 'Customized plans for corporate clients.', 'image': 'https://via.placeholder.com/150'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('marketplace'))
    return render_template('login.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return redirect(url_for('marketplace'))
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    import os
    os.environ["FLASK_RUN_RELOADER"] = "stat"
    app.run(debug=True)
