Online Bookstore Application Setup Guide
======================================

1. Project Structure
-------------------
bookstore/
├── venv/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── cart.html
│   └── book_detail.html
├── app.py
├── database.py
├── database.sql
├── requirements.txt
└── .gitignore

2. Initial Setup
---------------
a. Create Virtual Environment:
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate

b. Install Requirements:
   pip install -r requirements.txt

3. Database Setup
----------------
a. MySQL Installation:
   - Install MySQL if not already installed
   - Start MySQL service
   - Log in to MySQL:
     mysql -u root -p

b. Database Creation:
   - Copy contents of database.sql
   - Paste into MySQL console or run:
     mysql -u root -p < database.sql

c. Configure Database Connection:
   - Open database.py
   - Update credentials:
     host='localhost'
     user='root'  # Your MySQL username
     password='your_password'  # Your MySQL password
     database='bookstore'

4. Application Configuration
---------------------------
a. Secret Key:
   - Open app.py
   - Change the secret key:
     app.secret_key = 'your_secure_random_string'

5. Running the Application
-------------------------
a. Start the Server:
   python app.py
   
b. Access the Application:
   http://localhost:5000

6. Testing Features
------------------
a. User Registration:
   - Click "Register" in navigation
   - Fill required fields:
     * Username
     * Email
     * Full Name
     * Password
   - Submit form

b. User Login:
   - Click "Login" in navigation
   - Enter credentials:
     * Username
     * Password
   - Submit form

c. Browse Books:
   - View books on home page
   - Click book titles for details
   - Check images and descriptions

d. Shopping Cart:
   - Login required
   - Click "Add to Cart" on books
   - View cart contents
   - Check total calculation

e. Logout:
   - Click "Logout" in navigation
   - Verify session cleared

7. Troubleshooting
-----------------
a. Database Connection Issues:
   - Verify MySQL is running
   - Check credentials in database.py
   - Ensure database 'bookstore' exists

b. Image Loading Issues:
   - Verify image URLs in database
   - Check internet connection
   - Images are loaded from unsplash.com

c. Session Issues:
   - Clear browser cache
   - Verify secret key is set
   - Check Flask debug messages

8. Security Notes
----------------
- Passwords are hashed using Werkzeug
- Session data is encrypted
- SQL injection protected using parameterized queries
- CSRF protection via Flask-WTF (if added)

9. Features Overview
-------------------
Current Features:
- User authentication (register/login)
- Book browsing
- Shopping cart
- Session management
- Responsive design

Potential Additions:
- Payment processing
- Order history
- Book reviews
- Admin panel
- Search functionality
- Categories/filtering

10. File Descriptions
--------------------
app.py:
- Main application file
- Contains all routes and view functions
- Handles session management

database.py:
- Database connection management
- MySQL interaction wrapper

templates/:
- base.html: Base template with navigation
- index.html: Home page with book listing
- login.html: User login form
- register.html: User registration form
- cart.html: Shopping cart view
- book_detail.html: Individual book view

static/style.css:
- All application styling
- Responsive design rules
- Component-specific styles

11. Maintenance
--------------
Regular Tasks:
- Update dependencies
- Check database connections
- Monitor error logs
- Backup database
- Update book inventory

12. Development Notes
--------------------
Debug Mode:
- Currently enabled (app.run(debug=True))
- Shows detailed error messages
- Auto-reloads on code changes

Code Style:
- Following PEP 8 guidelines
- Using Flask conventions
- Modular structure for scalability 
