// Simulate database using a JSON object
let database = {
    users: [],
  };
  
  function loginWithEmail() {
      const username = document.getElementById('username').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
  
      // Check if user exists in the database
      const user = database.users.find(u => u.username === username && u.email === email && u.password === password);
  
      if (user) {
          alert('Login successful!');
          // Redirect to the dashboard or home page
      } else {
          alert('Invalid credentials. Please try again or sign up.');
      }
  }
  
  function loginWithGoogle() {
      // Implement Google sign-in functionality using Google API or Firebase Auth
      alert('Login with Google not implemented yet!');
  }
  
  function signup() {
      const username = document.getElementById('username').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
  
      // Check if the username or email already exists in the database
      const existingUser = database.users.find(u => u.username === username || u.email === email);
  
      if (existingUser) {
          alert('Username or email already exists. Please choose another.');
      } else {
          // Save the user to the database
          database.users.push({ username, email, password });
          alert('Account created successfully! You can now login.');
          // Redirect to the login page
          window.location.href = 'index.html';
      }
  }
  