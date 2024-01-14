
from flask import Flask
from flask_migrate import Migrate 
from models import db, User

app = Flask(__name__)

# configuring the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# link migrations 
migrations =  Migrate(app, db)

#  init the db
db.init_app(app)

@app.route('/')
def index():
    return "First Flask app "

