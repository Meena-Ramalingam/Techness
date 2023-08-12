from flask import Flask, render_template, request, redirect, url_for, jsonify, session, Response
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample product list (product code, product name, present count, minimum count, dealer, contact, order count, price)
products = [
    ("P001", "Product 1", 50, 20, "Dealer 1", "email", "dealer1@example.com", 100, 10.00),
    ("P002", "Product 2", 30, 10, "Dealer 2", "sms", "1234567890", 50, 20.00),
    # Add more products here
]

# Sample orders list (product code, quantity)
orders = []

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

@app.route('/product_list')
def product_list():
    return render_template('product_list.html', products=products)

@app.route('/create_bill', methods=['POST'])
def create_bill():
    total_amount = 0.0
    bill_items = []

    for product in products:
        code = product[0]
        name = product[1]
        quantity = int(request.form.get(f'{code}_quantity', 0))
        if quantity > 0:
            price = product[8]
            amount = price * quantity
            total_amount += amount
            bill_items.append((code, name, quantity, amount))
            update_present_count(code, quantity)

    gst_rate = 0.18  # GST rate of 18%
    discount = 10    # Discount in percentage

    gst_amount = total_amount * gst_rate
    discount_amount = total_amount * (discount / 100)
    final_amount = total_amount + gst_amount - discount_amount

    return render_template('invoice.html', bill_items=bill_items, total_amount=total_amount, gst_amount=gst_amount, discount_amount=discount_amount, final_amount=final_amount)


def update_present_count(product_code, quantity):
    for product in products:
        if product[0] == product_code:
            present_count = product[2]
            product_index = products.index(product)
            products[product_index] = (
                *product[:2],
                present_count - quantity,
                *product[3:]
            )
            if present_count - quantity <= product[3]:
                place_order(product)

def place_order(product):
    dealer_mode = product[5]
    dealer_contact = product[6]
    order_count = product[7]

    if dealer_mode == "email":
        send_email_order(dealer_contact, product[0], order_count)
    elif dealer_mode == "sms":
        send_sms_order(dealer_contact, product[0], order_count)

def send_email_order(email, product_code, order_count):
    subject = f"Order Request for Product {product_code}"
    body = f"Please send {order_count} units of Product {product_code}."
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "your_email@example.com"
    msg['To'] = email

    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail("your_email@example.com", [email], msg.as_string())
    server.quit()

def send_sms_order(phone_number, product_code, order_count):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone_number,
        from_='your_twilio_number',
        body=f"Please send {order_count} units of Product {product_code}."
    )
    
    
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
