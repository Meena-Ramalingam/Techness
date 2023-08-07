function signup() {
    const username = document.getElementById('signupUsername').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const userType = document.getElementById('userType').value;
    console.log(username, email, password, userType);
    $.ajax({
        url: 'signup.php',
        type: 'POST',
        dataType: 'json',
        data: {
            username: username,
            email: email,
            password: password,
            userType: userType
        },
        success: function (response) {
            $('#message').text(response.message);
            if (response.success) {
                // Redirect to the login page
                window.location.href = 'login.html';
            }
        },
        error: function () {
            $('#message').text('An error occurred. Please try again later.');
        }
    });
}
