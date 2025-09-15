# Techness

Techness is a Retailer-Wholesaler Platform designed to streamline stock management, order placement, and customer satisfaction for retail businesses.

## Features

- **User Authentication:** Retailers and wholesalers can sign up and log in.
- **Dashboard:** Overview of business operations and quick navigation.
- **Inventory Management:** Add, view, and delete products; track stock levels.
- **Dealer Information:** View dealer details and product associations.
- **Billing System:** Create bills, calculate GST, and update inventory.
- **Sales Prediction:** Visual insights for sales forecasting.
- **Automated Email Alerts:** Notifies dealers when stock falls below minimum levels.

## Technologies Used

- **Backend:** Python, Flask, SQLite
- **Frontend:** HTML, CSS (Poppins, Boxicons), JavaScript, jQuery
- **Email:** SMTP (Gmail)
- **SMS:** Twilio (optional)

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Techness.git
   cd Techness
   ```

2. **Install dependencies:**
   ```sh
   pip install flask twilio
   ```

3. **Initialize databases:**
   - Run `database.py` to create the user database.
   - Run `products.py` to populate the product database.

4. **Start the Flask server:**
   ```sh
   python app.py
   ```
   The app runs on [http://localhost:8000](http://localhost:8000).

## File Structure

- `app.py` — Main Flask application.
- `database.py` — User database initialization.
- `products.py` — Product database initialization.
- `static/` — CSS and images.
- `templates/` — HTML templates for all pages.

## Usage

- Visit `/signup` to create a new account.
- Log in at `/login`.
- Access dashboard, inventory, billing, dealers, and sales prediction via navigation links.

## License

MIT License

---

Techness: Retailer-Wholesaler Platform for Efficient Stock, Orders, and Customer Satisfaction.