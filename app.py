from flask import Flask, render_template, redirect, url_for, request
from web3 import Web3

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': 'Flight Delay Insurance A',
        'description': 'Comprehensive coverage for flight delays.',
        'price': 100,
        'image': 'https://via.placeholder.com/150'
    },
    # Add more products with unique 'id', 'name', 'description', 'price', and 'image' keys
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/connect_wallet')
def connect_wallet():
    return render_template('connect_wallet.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html', products=products)

@app.route('/profile')
def profile():
    user_profile = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'purchases': ['Flight Delay Insurance A', 'Flight Delay Insurance B']
    }
    return render_template('profile.html', profile=user_profile)

@app.route('/profile/edit', methods=['GET', 'POST'])
def profile_edit():
    if request.method == 'POST':
        profile['name'] = request.form['name']
        profile['email'] = request.form['email']
        return redirect(url_for('profile'))
    return render_template('profile_edit.html', profile=profile)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return 'Product not found', 404

if __name__ == '__main__':
    app.run(debug=True)




