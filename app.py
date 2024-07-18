from flask import Flask, render_template, redirect, url_for, request, session
from web3 import Web3
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Ethereum client connection
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Sample smart contract (replace with your own)
contract_address = 'YOUR_SMART_CONTRACT_ADDRESS'
#contract_abi = json.loads('YOUR_CONTRACT_ABI')

# Simulated user data
user_profile = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'wallet': '0x1234567890abcdef1234567890abcdef12345678'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/connect_wallet')
def connect_wallet():
    return render_template('connect_wallet.html')

@app.route('/marketplace')
def marketplace():
    products = [
        {'id': 1, 'name': 'Flight Delay Insurance', 'price': '0.005 ETH'},
        {'id': 2, 'name': 'Baggage Loss Insurance', 'price': '0.02 ETH'},
        {'id': 3, 'name': 'Travel Cancellation Insurance', 'price': '0.03 ETH'},
        {'id': 4, 'name': 'Medical Travel Insurance', 'price': '0.04 ETH'},
        {'id': 5, 'name': 'Trip Interruption Insurance', 'price': '0.05 ETH'},
        {'id': 6, 'name': 'Travel Accident Insurance', 'price': '0.06 ETH'},
        {'id': 7, 'name': 'Emergency Evacuation Insurance', 'price': '0.07 ETH'},
        {'id': 8, 'name': 'Travel Delay Insurance', 'price': '0.08 ETH'},
    ]
    return render_template('marketplace.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Mock data for demonstration
    product = {'id': product_id, 'name': f'Product {product_id}', 'price': f'{0.01 * product_id} ETH'}
    return render_template('product_detail.html', product=product)

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=user_profile)

@app.route('/profile/edit', methods=['GET', 'POST'])
def profile_edit():
    if request.method == 'POST':
        user_profile['name'] = request.form['name']
        user_profile['email'] = request.form['email']
        return redirect(url_for('profile'))
    return render_template('profile_edit.html', profile=user_profile)

@app.route('/buy_product', methods=['POST'])
def buy_product():
    product_id = request.form.get('product_id')
    wallet_address = session.get('wallet_address')
    if not wallet_address:
        return redirect(url_for('connect_wallet'))

    # Transaction details
    product_price = web3.toWei(0.01 * int(product_id), 'ether')
    nonce = web3.eth.getTransactionCount(wallet_address)
    txn = {
        'to': contract_address,
        'value': product_price,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
        'chainId': 1
    }
    return render_template('transaction.html', txn=txn)

@app.route('/disconnect_wallet')
def disconnect_wallet():
    session.pop('wallet_address', None)
    return redirect(url_for('connect_wallet'))

if __name__ == '__main__':
    app.run(debug=True)



