from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Zeke'} #this is zeke
    posts = [
        {
            'author': {'nickname': 'Zeke'},
            'body': 'today is a day and outside is still there'
        },
        {
            'author': {'nickname': 'Bobert'},
            'body': 'the movie i like is not bad'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
