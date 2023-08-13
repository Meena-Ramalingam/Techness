import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('product_database.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        product_code TEXT,
        product_name TEXT,
        price_per_piece REAL,
        present_stock INTEGER,
        minimum_stock INTEGER,
        dealer_name TEXT,
        dealer_email TEXT,
        dealer_order_count INTEGER
    )
''')
def insert_product(conn, product_data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (
            product_code, product_name, price_per_piece, present_stock,
            minimum_stock, dealer_name, dealer_email, dealer_order_count
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', product_data)
    conn.commit()

# Connect to the database


# Example product data (product_code, product_name, price_per_piece, present_stock, minimum_stock, dealer_name, dealer_email, dealer_order_count)
# Example product data (product_code, product_name, price_per_piece, present_stock, minimum_stock, dealer_name, dealer_email, dealer_order_count)
product_data_list = [
    ('P001', 'Sankar Cement', 12.99, 500, 100, 'Cement Suppliers', '211501049@rajalakshmi.edu.in', 10),
    ('P002', 'Asian Paints - White', 25.50, 200, 50, 'Paints Inc.', '211501020@rajalakshmi.edu.in', 5),
    ('P003', 'Electrical Switch', 3.99, 1000, 200, 'Electro World', '211501051@rajalakshmi.edu.in', 50),
    ('P004', 'Hammer', 8.95, 150, 20, 'Tool Masters', '211501011@rajalakshmi.edu.in', 15),
    ('P005', 'Screwdriver Set', 6.75, 300, 50, 'Tool Masters', 'tools@example.com', 10),
    ('P006', 'Door Lock', 14.50, 100, 10, 'Security Supplies', 'security@example.com', 5),
    ('P007', 'Wood Glue', 4.25, 400, 50, 'Adhesive Co.', 'adhesive@example.com', 25),
    ('P008', 'PVC Pipes (3m)', 2.99, 600, 100, 'Plumbing Depot', 'plumbing@example.com', 30),
    ('P009', 'Paint Brushes Set', 9.75, 250, 30, 'Paints Inc.', 'paints@example.com', 8),
    ('P010', 'Power Drill', 55.00, 50, 10, 'Tool Masters', 'tools@example.com', 2),
    ('P011', 'Ceiling Fan', 29.99, 100, 20, 'Electro World', 'electro@example.com', 5),
    ('P012', 'Nails (1kg)', 1.50, 800, 100, 'Hardware Supplies', 'hardware@example.com', 40),
    ('P013', 'Hacksaw', 7.25, 120, 15, 'Tool Masters', 'tools@example.com', 10),
    ('P014', 'Paint Roller', 5.50, 180, 30, 'Paints Inc.', 'paints@example.com', 12),
    ('P015', 'Plunger', 3.25, 50, 5, 'Plumbing Depot', 'plumbing@example.com', 2),
    ('P016', 'Extension Cord', 8.99, 200, 30, 'Electro World', 'electro@example.com', 10),
    ('P017', 'Sanding Paper (Pack)', 3.75, 350, 50, 'Hardware Supplies', 'hardware@example.com', 20),
    ('P018', 'Tape Measure', 4.50, 100, 10, 'Tool Masters', 'tools@example.com', 5),
    ('P019', 'Cordless Screwdriver', 29.95, 80, 15, 'Tool Masters', 'tools@example.com', 3),
    ('P020', 'Plastic Tarpaulin', 12.25, 150, 25, 'Hardware Supplies', 'hardware@example.com', 8),
    ('P021', 'Window Lock', 6.99, 90, 10, 'Security Supplies', 'security@example.com', 4),
    ('P022', 'LED Light Bulbs (Pack)', 10.50, 300, 50, 'Electro World', 'electro@example.com', 15),
    ('P023', 'Pipe Wrench', 9.25, 70, 10, 'Plumbing Depot', 'plumbing@example.com', 5),
    ('P024', 'Safety Gloves', 2.99, 400, 50, 'Safety Gear Co.', 'safety@example.com', 30),
    ('P025', 'Angle Grinder', 65.00, 30, 5, 'Tool Masters', 'tools@example.com', 2),
    ('P026', 'Paint Thinner', 6.25, 250, 30, 'Paints Inc.', 'paints@example.com', 20),
    ('P027', 'Door Handle', 8.50, 120, 15, 'Hardware Supplies', 'hardware@example.com', 10),
    ('P028', 'Caulking Gun', 4.75, 150, 20, 'Adhesive Co.', 'adhesive@example.com', 8),
    ('P029', 'Wrench Set', 12.99, 180, 25, 'Tool Masters', 'tools@example.com', 12),
    ('P030', 'Smoke Detector', 18.50, 70, 10, 'Security Supplies', 'security@example.com', 4),
    ('P031', 'Copper Wire (Roll)', 3.50, 400, 50, 'Electro World', 'electro@example.com', 25),
    ('P032', 'Pipe Insulation (Pack)', 7.25, 250, 30, 'Plumbing Depot', 'plumbing@example.com', 15),
    ('P033', 'Work Gloves', 2.75, 300, 50, 'Safety Gear Co.', 'safety@example.com', 20),
    ('P034', 'Circular Saw', 48.00, 40, 5, 'Tool Masters', 'tools@example.com', 3),
    ('P035', 'Grout Sealer', 5.25, 180, 25, 'Adhesive Co.', 'adhesive@example.com', 10),
    ('P036', 'Ladder (6ft)', 32.99, 70, 10, 'Hardware Supplies', 'hardware@example.com', 5),
    ('P037', 'Drain Snake', 9.75, 120, 15, 'Plumbing Depot', 'plumbing@example.com', 8),
    ('P038', 'First Aid Kit', 18.50, 50, 5, 'Safety Gear Co.', 'safety@example.com', 4),
    ('P039', 'Angle Iron (6ft)', 6.99, 200, 30, 'Hardware Supplies', 'hardware@example.com', 15),
    ('P040', 'Chisel Set', 5.75, 180, 25, 'Tool Masters', 'tools@example.com', 10),
    ('P041', 'Bolt Cutter', 12.99, 90, 10, 'Tool Masters', 'tools@example.com', 6),
    ('P042', 'Duct Tape (Roll)', 2.50, 300, 50, 'Adhesive Co.', 'adhesive@example.com', 20),
    ('P043', 'Step Stool', 14.99, 70, 10, 'Hardware Supplies', 'hardware@example.com', 5),
    ('P044', 'Plumber\'s Putty', 3.25, 250, 30, 'Plumbing Depot', 'plumbing@example.com', 15),
    ('P045', 'Safety Goggles', 4.50, 180, 25, 'Safety Gear Co.', 'safety@example.com', 12),
    ('P046', 'Pliers Set', 12.75, 120, 15, 'Tool Masters', 'tools@example.com', 10),
    ('P047', 'Broom', 5.25, 200, 30, 'Hardware Supplies', 'hardware@example.com', 12),
    ('P048', 'Cable Ties (Pack)', 1.99, 400, 50, 'Electro World', 'electro@example.com', 30),
    ('P049', 'Tape Gun', 3.75, 150, 20, 'Adhesive Co.', 'adhesive@example.com', 10),
    ('P050', 'Step Ladder (4ft)', 22.50, 100, 15, 'Hardware Supplies', 'hardware@example.com', 5),
]

# Insert the product data
for product_data in product_data_list:
    insert_product(conn, product_data)



# Commit the changes and close the connection
conn.commit()
conn.close()
