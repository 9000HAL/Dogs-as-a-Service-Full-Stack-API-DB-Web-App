from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://habrpuql:PggYGrzmBoFFYntRSRSMstXjCYm6mmxi@bubble.db.elephantsql.com/habrpuql'

db = SQLAlchemy(app)




@app.route('/')
def hello_world():
    return 'Hello, LB!'

if __name__ == '__main__':
    app.run()
