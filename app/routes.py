from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ian'}
    posts = [
                {'author': {'username': 'Ian'},
                 'body': 'Beautiful day in Peckham'
                 },
                {'author': {'username': 'Jack'},
                 'body': 'Ride the train in Rio'
                 }
            ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)
