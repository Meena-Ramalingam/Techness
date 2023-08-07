function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    $.ajax({
        url: 'login.php',
        type: 'POST',
        dataType: 'json',
        data: {
            username: username,
            password: password
        },
        success: function (response) {
            $('#message').text(response.message);
            if (response.success) {
                // Redirect to the dashboard or home page
                window.location.href = 'dashboard.html';
            }
        },
        error: function () {
            $('#message').text('An error occurred. Please try again later.');
        }
    });
}
