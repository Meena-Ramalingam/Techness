let database = {
    users: [],
  };
  
  // Function to sign up a new user and store their data in the "database"
  function signup() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const userType = document.getElementById('userType').value; // Assuming you have a select input with options for "retailer" and "wholesaler"
  
    // Check if the username or email already exists in the "database"
    const existingUser = database.users.find(u => u.username === username || u.email === email);
  
    if (existingUser) {
      alert('Username or email already exists. Please choose another.');
    } else {
      // Save the user to the "database" with username, email, password, and userType
      database.users.push({ username, email, password, userType });
  
      alert('Account created successfully! You can now login.');
      // Redirect to the login page
      window.location.href = 'index.html';
    }
  }
  // Function to log in an existing user
function loginWithEmail() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    // Check if user exists in the "database"
    const user = database.users.find(u => u.email === email && u.password === password);
  
    if (user) {
      alert('Login successful! Redirecting...');
  
      // Redirect to the appropriate page based on user type
      if (user.userType === 'retailer') {
        window.location.href = 'retailer_dashboard.html'; // Redirect to the retailer dashboard
      } else if (user.userType === 'wholesaler') {
        window.location.href = 'wholesaler_dashboard.html'; // Redirect to the wholesaler dashboard
      } else {
        alert('Invalid user type.'); // Handle the case where user type is neither retailer nor wholesaler
      }
    } else {
      alert('Invalid credentials. Please try again or sign up.');
    }
  }
  