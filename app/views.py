from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')

@app.route('/feed')
def feed():
    user = {'nickname': 'Rich'} 
    posts = [
        {
            'author': {'nickname': 'Bob'},
            'body': 'i am going to send my children to school one day'
        },
        {
            'author': {'nickname': 'Bill'},
            'body': 'i like to do machine learning and this can use machine learning'
        },
        {
            'author': {'nickname': 'Bryan'},
            'body': 'the frontend of this is cool like stuff i do'
        },
        {
            'author': {'nickname': 'Bryn'},
            'body': 'this is a great tool that i like'
        }
    ]
    return render_template('feed.html',
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/calendar')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/data')
def data():
    user = {'nickname': 'hayden'} 
    posts = [
        {
            'author': {'nickname': 'Hayden'},
            'body': 'today is a day and outside is still there'
        },
    ]
    return render_template('data.html',
                           title='Data',
                           user=user,
                           posts=posts)

