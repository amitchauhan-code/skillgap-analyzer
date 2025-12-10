from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your-super-secret-key-change-this-later'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Chauhan@123'       
app.config['MYSQL_DB'] = 'skillgap'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                        (username, email, password))
            mysql.connection.commit()
            cur.close()
            flash('Account created successfully! Now login.', 'success')
            return redirect(url_for('login'))
        except:
            flash('Username or Email already exists!', 'danger')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        if user:
            session['loggedin'] = True
            session['username'] = user['username']
            session['user_id'] = user['id']
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/evaluate')
def evaluate():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('evaluate.html', username=session['username'])

# ==================== QUIZ ROUTES ====================
@app.route('/quiz/web')
def quiz_web():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('quiz_web.html', username=session['username'])

@app.route('/quiz/data')
def quiz_data():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('quiz_data.html', username=session['username'])

@app.route('/quiz/uiux')
def quiz_uiux():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('quiz_uiux.html', username=session['username'])

# ==================== ANALYSIS & COURSES ====================
@app.route('/analysis')
def analysis():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    # Ye baad mein quiz se real score se aayega – abhi dummy data
    skills = {
        'HTML': 90,
        'CSS': 85,
        'JavaScript': 65,
        'Python': 45,
        'React': 30,
        'Bootstrap': 75,
        'Git': 55
    }
    return render_template('analysis.html', skills=skills, username=session['username'])

@app.route('/courses')
def courses():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    recommended = [
        {"title": "The Complete Web Development Bootcamp 2025", "platform": "Udemy", "link": "https://www.udemy.com/course/the-complete-web-development-bootcamp/", "price": "₹499"},
        {"title": "HTML CSS JavaScript – Full Course", "platform": "YouTube - CodeWithHarry", "link": "https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg", "price": "Free"},
        {"title": "Python Full Course for Beginners", "platform": "YouTube - Mosh", "link": "https://youtu.be/kqtD5dpn9C8", "price": "Free"},
        {"title": "React JS Crash Course 2025", "platform": "YouTube - Traversy Media", "link": "https://youtu.be/w7ejDZ8SWv8", "price": "Free"},
        {"title": "Full Stack Web Development", "platform": "PW Skills", "link": "https://pwskills.com/course/Full-Stack-web-development", "price": "₹3499"},
        {"title": "100 Days of Code – Web Development", "platform": "YouTube - Angela Yu", "link": "https://youtu.be/Oev2Xq8p6dw", "price": "Free"}
    ]
    return render_template('courses.html', courses=recommended, username=session['username'])

# ==================== LOGOUT & OTHERS ====================
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 