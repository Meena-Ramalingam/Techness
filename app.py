from flask import Flask, json,render_template, request, redirect, url_for, jsonify, session, Response
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import sqlite3


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USER = 'meenaramalingamspr@gmail.com'
EMAIL_PASSWORD = 'harishankar826'


@app.route('/')
def home():
    return render_template('login.html')



@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    user_type = request.form.get('userType')

    # Establish a connection to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the username already exists in the database
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return jsonify({"success": False, "message": "Username already exists."})

    try:
        print("trying")
        # Insert the new user into the database
        cursor.execute('INSERT INTO users (username, password, email, userType) VALUES (?, ?, ?, ?)',
                       (username, password, email, user_type))
        conn.commit()
        conn.close()
        # return redirect(url_for('login'))
        

        return jsonify({"success": True, "message": "Sign up successful!"})
    
    except Exception as e:
        print("An error occurred:", str(e))
        conn.close()
        return jsonify({"success": False, "message": "Sign up failed. An error occurred."})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # email = request.form.get('email')

        # Establish a connection to the SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Check if the provided username, password, and user type match in the database
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()

        
        if user:
            session['username'] = username
            return jsonify({"redirect": url_for('dashboard')})  # Redirect to dashboard or other page
        else:
            return jsonify({"message": "Invalid credentials. Please try again."})
        
    return render_template('login.html')

    
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT product_code, product_name, present_stock, minimum_stock FROM products')
    inventory = cursor.fetchall()
    conn.close()
    return jsonify(inventory)

@app.route('/dealers')
def dealers():
    return render_template('dealers.html')

@app.route('/get_dealers', methods=['GET'])
def get_dealers():
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT dealer_name, dealer_email, product_code, product_name, dealer_order_count FROM products')
    dealers = cursor.fetchall()
    conn.close()
    return jsonify(dealers)


def fetch_product_data(product_code):
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT product_name, price_per_piece FROM products WHERE product_code = ?
    ''', (product_code,))
    row = cursor.fetchone()
    conn.close()
    return row
def send_email(subject, message, recipient):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = recipient

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, recipient, msg.as_string())

        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

@app.route('/billing')
def billing():
    return render_template('billing.html')

@app.route('/submit_bill', methods=['POST'])
def submit_bill():
    data = request.json.get('product_data')  # Retrieve JSON data from the request
    
    # Process and update the database based on the JSON data
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()

    for product in data:
        product_code = product['product_code']
        quantity = product['quantity']

        # Fetch the current present_stock for the product
        cursor.execute('SELECT minimum_stock,present_stock FROM products WHERE product_code = ?', (product_code,))
        row = cursor.fetchone()

        if row is not None:
            current_stock, minimum_stock = row
            new_stock = current_stock - int(quantity)
            cursor.execute('UPDATE products SET present_stock = ? WHERE product_code = ?', (new_stock, product_code))
        if new_stock <= minimum_stock: # type: ignore
            dealer_email = 'dealer@example.com'  # Replace with the actual dealer's email
            product_name = fetch_product_data(product_code)[0]
            subject = f'Product Reorder: {product_name}'
            message = f"Please place an order for {quantity} units of {product_name} within 2 days."
            send_email(subject, message, dealer_email)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Redirect to the "Thank You" page
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/get_product_data', methods=['POST'])
def get_product_data():
    product_code = request.json.get('product_code')
    product_data = fetch_product_data(product_code)
    return jsonify({'product_name': product_data[0], 'price': product_data[1]})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
