<?php
// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Read the incoming JSON data
    $json_data = file_get_contents('php://input');
    $invoice_data = json_decode($json_data, true);

    // Database credentials
    $host = 'localhost'; // e.g., 'localhost'
    $username = 'root';
    $password = '';
    $database = 'techdb';

    // Connect to the database
    $conn = new mysqli($host, $username, $password, $database);

    // Check connection
    if ($conn->connect_error) {
        die('Connection failed: ' . $conn->connect_error);
    }

    // Extract data from the invoice_data array
    $cartItems = $invoice_data['cartItems'];
    $subtotal = $invoice_data['subtotal'];
    $discount = $invoice_data['discount'];
    $total = $invoice_data['total'];

    // Prepare and execute SQL queries to save data in the database
    // Note: This code is a basic example. In a real application, you should use prepared statements to prevent SQL injection.

    // Save invoice data
    $sql_invoice = "INSERT INTO invoices (subtotal, discount, total) VALUES ('$subtotal', '$discount', '$total')";
    if ($conn->query($sql_invoice) !== TRUE) {
        echo 'Error saving invoice data: ' . $conn->error;
        exit;
    }

    // Get the last inserted invoice ID
    $invoice_id = $conn->insert_id;

    // Save cart items data
    foreach ($cartItems as $item) {
        $product = $item['product'];
        $quantity = $item['quantity'];
        $price = $item['price'];
        $total = $item['total'];

        $sql_cart_item = "INSERT INTO cart_items (invoice_id, product, quantity, price, total) VALUES ('$invoice_id', '$product', '$quantity', '$price', '$total')";
        if ($conn->query($sql_cart_item) !== TRUE) {
            echo 'Error saving cart item data: ' . $conn->error;
            exit;
        }
    }

    // Close the database connection
    $conn->close();

    // Send a success response
    $response = array('status' => 'success', 'message' => 'Invoice data saved successfully');
    echo json_encode($response);
} else {
    // Invalid request method
    http_response_code(405);
    $response = array('status' => 'error', 'message' => 'Invalid request method');
    echo json_encode($response);
}
?>
