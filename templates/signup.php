<?php
require_once('db_connection.php');

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $userType = $_POST['userType'];

    // Sanitize input to prevent SQL injection (use mysqli_real_escape_string or prepared statements)
    $username = mysqli_real_escape_string($conn, $username);
    $email = mysqli_real_escape_string($conn, $email);
    $password = mysqli_real_escape_string($conn, $password);
    $userType = mysqli_real_escape_string($conn, $userType);

    // Check if the username or email already exists in the database
    $query = "SELECT * FROM users WHERE username = '$username' OR email = '$email'";
    $result = $conn->query($query);

    if ($result->num_rows > 0) {
        echo json_encode(["success" => false, "message" => "Username or email already exists. Please choose another."]);
    } else {
        // Save the user to the database
        $query = "INSERT INTO users (username, email, password, user_type) VALUES ('$username', '$email', '$password', '$userType')";
        if ($conn->query($query)) {
            echo json_encode(["success" => true, "message" => "Account created successfully! You can now login."]);
        } else {
            echo json_encode(["success" => false, "message" => "Error creating account. Please try again later."]);
        }
    }
}
?>
