from flask import Flask, render_template
# import config
#v.2 above ^^^^^^^^^^^^^^^^^^^^^^see above config SGUIGGGLY --- !!!!!!!!!!!!!!!!!!!!!!

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres://habrpuql:PggYGrzmBoFFYntRSRSMstXjCYm6mmxi@bubble.db.elephantsql.com/habrpuql'

db = SQLAlchemy(app)



#v.2 do next ----------------------

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


















# v.1 to delete next ---------------------- renders SUCCESSFULLY

""" 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
"""
# v.1 to delete next ----------------------


