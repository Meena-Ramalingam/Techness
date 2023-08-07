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
  