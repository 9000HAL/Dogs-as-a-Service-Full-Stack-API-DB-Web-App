from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Make sure to import this
import requests
import config
from flask import render_template, request, redirect, url_for, flash #documentation reccomend....?
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



app = Flask(__name__)
app.config.from_object(config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://habrpuql:PggYGrzmBoFFYntRSRSMstXjCYm6mmxi@bubble.db.elephantsql.com/habrpuql' = NO WORKS DO NOT USE 
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'



@app.route('/')
def hello_world():
    return 'Hello, LB!'

if __name__ == '__main__':
    app.run()



@app.route('/add_user/<username>/<email>', methods=['GET'])
def add_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f'User {new_user.username} added.'



@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return '<br>'.join([f'User: {user.username}, Email: {user.email}' for user in users])



@app.route('/update/<username>/<new_email>', methods=['GET'])
def update_user(username, new_email):
    user = User.query.filter_by(username=username).first()
    if user:
        user.email = new_email
        db.session.commit()
        return f'Email updated to {new_email}.'
    else:
        return f'User {username} does not exist.'



@app.route('/delete/<username>', methods=['GET'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return f'User {username} deleted.'
    else:
        return f'User {username} does not exist.'



@app.route('/random_dog', methods=['GET'])
def random_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    return f"<img src='{data['message']}'>"
