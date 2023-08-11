function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const userType = document.getElementById('userType').value;

    $.ajax({
        url: 'login.php',
        type: 'POST',
        dataType: 'json',
        data: {
            username: username,
            password: password,
            userType: userType
        },
        success: function (response) {
            $('#message').text(response.message);
            if (response.success) {
                // Redirect to the dashboard or home page
                // window.location.href = 'dashboard.html';
                if (userType === 'retailer') {
                    // Redirect to retailer dashboard after successful login
                    window.location.href = 'dashboard.html';
                } else if (userType === 'wholesaler') {
                    // Redirect to wholesaler dashboard after successful login
                    window.location.href = 'wholesaler_dashboard.html';
                }
            }
        },
        error: function () {
            $('#message').text('An error occurred. Please try again later.');
        }
    });
}
