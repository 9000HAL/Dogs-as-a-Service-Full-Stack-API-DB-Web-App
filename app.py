from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Make sure to import this

import config



app = Flask(__name__)
app.config.from_object(config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://habrpuql:PggYGrzmBoFFYntRSRSMstXjCYm6mmxi@bubble.db.elephantsql.com/habrpuql'
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


