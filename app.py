from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date,datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

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



# Sample data for news headlines
sample_headlines = [
    {
        "headline": "Breaking News: Major Earthquake Hits Eastern Region",
        "description": "A major earthquake with a magnitude of 7.5 struck the eastern region...",
        "author": "John Doe",
        "category": "Disaster"
    },
    {
        "headline": "Sports: Team Wins Championship in Thrilling Overtime",
        "description": "The local sports team secured a stunning victory in the championship...",
        "author": "Jane Smith",
        "category": "Sports"
    },
    {
        "headline": "Lifestyle: New Fashion Trends for This Season",
        "description": "Discover the latest fashion trends for this season and upgrade your wardrobe...",
        "author": "Samantha Johnson",
        "category": "Lifestyle"
    },
    {
        "headline": "Technology: Launch of Revolutionary AI-powered Device",
        "description": "A groundbreaking AI-powered device is set to change the tech industry...",
        "author": "Michael Lee",
        "category": "Technology"
    },
    {
        "headline": "Health: Tips for a Balanced Diet and Exercise",
        "description": "Learn how to maintain a balanced diet and incorporate regular exercise...",
        "author": "Emily Wang",
        "category": "Health"
    }
]

@app.route('/')
def index():
    name = 'The BroadCast'
    launch_date = date.today()
    return render_template('base.html', name=name, date=launch_date)

@app.route('/news')
def news():
    return render_template('news.html', news_list=sample_headlines)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        headline = request.form['headline']
        description = request.form['description']
        author = request.form['author']
        category = request.form['category']
        return redirect('/news')
    else:
        return render_template('add_news.html') 

if __name__ == '__main__':
    app.run(debug=True)
