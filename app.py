from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date,datetime
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#for logging
logging.basicConfig(filename='website_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(10), nullable=False)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.context_processor
def inject_user_role():
    username = session.get('role')
    return dict(username=username)

@app.route('/')
def index():
    name = 'The BroadCast'
    launch_date = date.today()
    return render_template('base.html', name=name, date=launch_date, )

@app.route('/news' , methods=['GET', 'POST'])
def news():
    #get all news from database
    news_list = News.query.all()
    return render_template('news.html', news_list=news_list,)  

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/view_logs', methods=['GET'])
def view_logs():
    # Check if the user is logged in and has admin role
    if 'username' in session and session['role'] == 'admin':
        try:
            with open('website_logs.log', 'r') as log_file:
                logs = log_file.read()
                return render_template('view_logs.html', logs=logs)
        except FileNotFoundError:
            return render_template('view_logs.html', logs='Log file not found.')
    else:
        return 'You are not authorized to view this page.', 403


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        headline = request.form['headline']
        description = request.form['description']
        author = request.form['author']
        category = request.form['category']
        print(headline, description, author, category)
        news = News(headline=headline, description=description, author=author, category=category)
        db.session.add(news)
        db.session.commit()
        logging.info(f'News added by "{session["username"]}". Headline: "{headline}".')
        return redirect('/news')
    else:
        return render_template('add_news.html') 

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    news = News.query.get(id)
    if request.method == 'POST':
        news.headline = request.form['headline']
        news.description = request.form['description']
        news.author = request.form['author']
        news.category = request.form['category']
        db.session.commit()
        logging.info(f'News updated by "{session["username"]}". News ID: {news_id}.')
        return redirect('/news')
    else:
        return render_template('update.html', news=news)
@app.route('/delete/<int:id>')
def delete(id):
    news = News.query.get(id)
    db.session.delete(news)
    db.session.commit()
    return redirect('/news')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = User.query.filter_by(username=username, password=password).first()
        if user_data is not None:
            logging.info(f'User "{username}" logged in.')
            session['username'] = username
            session['role'] = user_data.role
            return redirect('/news')
        else:
            logging.warning(f'Failed login attempt for user "{username}".')
            msg = 'Invalid username or password'
            return render_template('login.html', msg= msg)
    else:
        username = session.get('username')
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        rpassword = request.form['rpassword']
        if password == rpassword:
            user = User(username=username, password=password, role='user')
            db.session.add(user)
            db.session.commit()
            flash('User registered successfully')
        return redirect('/news')
    else:
        return render_template('registration.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect('/news')

if __name__ == '__main__':
    app.run(debug=True)
