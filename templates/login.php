<?php
require_once('db_connection.php');
error_reporting(E_ALL); ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $userType = $_POST['userType'];

    // Sanitize input to prevent SQL injection (use mysqli_real_escape_string or prepared statements)
    $username = mysqli_real_escape_string($conn, $username);
    $password = mysqli_real_escape_string($conn, $password);
    $userType = mysqli_real_escape_string($conn, $userType);

    // Check if user exists in the database
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password' AND user_type = '$userType'";
    $result = $conn->query($query);

    if ($result->num_rows > 0) {
        echo json_encode(["success" => true, "message" => "Login successful!"]);
    } else {
        echo json_encode(["success" => false, "message" => "Invalid credentials. Please try again or sign up."]);
    }
}
?>
