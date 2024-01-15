# 1. import flask 
from flask import Flask

#  8. import flask migrate 
from flask_migrate import Migrate 
from models import db, User

#  2. create an instance for flask after we've pip installed it 
app = Flask(__name__)

# 7. configuring the app w/ app.config (frm 6 in models.py)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'

# 9. link migrations (after running pip install flask_migrate)
#  this takes two args ie the app and the db
migrations =  Migrate(app, db)

# 10. init the db
db.init_app(app)

# 3. Define an initial route
#  at this stage if you do flask run and navigate to that link you will see your flask app
@app.route('/')
def index():
    return "First Flask app "
 
