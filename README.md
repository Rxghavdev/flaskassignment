<!DOCTYPE html>
<html>
<head>

</head>
<body>
  <h1>Assignment for Corider</h1>
  <p>
    Welcome to my Flask application! This application demonstrates various features of Flask and interacts with a MongoDB database.
  </p>

  <h2>Installation</h2>
  <p>
    To run this application, follow these steps:
  </p>
  <code>
    git clone https://github.com/Rxghavdev/flaskassignment.git
    cd flaskassignment
    source path/to/venv/bin/activate
    pip install -r requirements.txt
    python app.py
  </code>

  <h2>API Endpoints</h2>
  <p>
    Here are the API endpoints available in this application:
  </p>
  <table>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>/</td>
      <td>GET</td>
      <td>Test database connection</td>
    </tr>
    <tr>
      <td>/users</td>
      <td>GET</td>
      <td>Retrieve all users</td>
    </tr>
    <tr>
      <td>/users</td>
      <td>POST</td>
      <td>Create a new user</td>
    </tr>
    <tr>
      <td>/users/&lt;id&gt;</td>
      <td>GET</td>
      <td>Retrieve a single user by ID</td>
    </tr>
    <tr>
      <td>/users/&lt;id&gt;</td>
      <td>PUT</td>
      <td>Update a user by ID</td>
    </tr>
    <tr>
      <td>/users/&lt;id&gt;</td>
      <td>DELETE</td>
      <td>Delete a user by ID</td>
    </tr>
  </table>

 <h2>Screenshots</h2>
<p>
  Here are some screenshots of API requests made to the application:
</p>

<h3>GET Request to Retrieve All Users</h3>
<p>
  <img src="![Screenshot from 2023-07-31 18-34-58](https://github.com/Rxghavdev/flaskassignment/assets/94173505/e292c50b-7664-4894-bacc-a0b11106da2d)
" alt="GET Request to Retrieve All Users">
</p>

<h3>POST Request to Create a New User</h3>
<p>
  <img src="![Screenshot from 2023-07-31 18-32-42](https://github.com/Rxghavdev/flaskassignment/assets/94173505/bf113dfc-4f22-498c-a2ee-3bebeca5eb6a)
 alt="POST Request to Create a New User">
</p>

<h3>GET Request to Retrieve a Single User by ID</h3>
<p>
  <img src="![image](https://github.com/Rxghavdev/flaskassignment/assets/94173505/35e0f7d8-3d2c-43b0-b635-f6e7a984c535)
" alt="GET Request to Retrieve a Single User by ID">
</p>

<h3>PUT Request to Update a User by ID</h3>
<p>
  <img src="![Screenshot from 2023-07-31 18-35-44](https://github.com/Rxghavdev/flaskassignment/assets/94173505/e71b6921-b2d0-463a-8153-c00ee753e8ae)
" alt="PUT Request to Update a User by ID">
</p>

<h3>DELETE Request to Delete a User by ID</h3>
<p>
  <img src="![Screenshot from 2023-07-31 18-35-23](https://github.com/Rxghavdev/flaskassignment/assets/94173505/e1641864-9089-409e-bef9-0ecad179e64f)
" alt="DELETE Request to Delete a User by ID">
</p>


  <h2>Technologies Used</h2>
  <ul>
    <li>Flask</li>
    <li>MongoDB</li>
    <li>HTML, CSS, JavaScript (for frontend, if applicable)</li>
    <li>...</li>
  </ul>

  <h2>License</h2>
  <p>
    This project is licensed under the MIT License - see the LICENSE file for details.
  </p>

  <h2>Contributing</h2>
  <p>
    Contributions are welcome! Fork the repository and create a pull request with your changes.
  </p>
</body>
</html>
