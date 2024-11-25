from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import Database
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_actual_secret_key_here'

@app.route('/')
def home():
    db = Database()
    db.cursor.execute("SELECT * FROM books")
    books = db.cursor.fetchall()
    db.close()
    return render_template('index.html', books=books)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = Database()
        db.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = db.cursor.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        
        flash('Invalid username or password', 'error')
        db.close()
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        full_name = request.form['full_name']
        
        hashed_password = generate_password_hash(password)
        
        db = Database()
        try:
            db.cursor.execute("""
                INSERT INTO users (username, password, email, full_name)
                VALUES (%s, %s, %s, %s)
            """, (username, hashed_password, email, full_name))
            db.conn.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except Error as e:
            flash('Registration failed!', 'error')
        finally:
            db.close()
    return render_template('register.html')

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    db = Database()
    db.cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
    book = db.cursor.fetchone()
    db.close()
    return render_template('book_detail.html', book=book)

@app.route('/add_to_cart/<int:book_id>')
def add_to_cart(book_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(book_id)
    flash('Book added to cart!', 'success')
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    if 'cart' not in session:
        session['cart'] = []
    
    db = Database()
    cart_items = []
    total = 0
    
    for book_id in session['cart']:
        db.cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
        book = db.cursor.fetchone()
        if book:
            cart_items.append(book)
            total += float(book['price'])
    
    db.close()
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 