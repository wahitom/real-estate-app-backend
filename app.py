# 1. import flask 
from flask import Flask

#  8. import flask migrate 
from flask_migrate import Migrate 

#  13. Import flask restful (12 from models.py) afterpip installing it 
from flask_restful import Api, Resource

from models import db, User
#  17. import location from resources folder(16 in resources)
from resources.location import Location



#  2. create an instance for flask after we've pip installed it 
app = Flask(__name__)

# 7. configuring the app w/ app.config (frm 6 in models.py)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'

# 9. link migrations (after running pip install flask_migrate)
#  this takes two args ie the app and the db
migrations =  Migrate(app, db)

# 10. init the db
db.init_app(app)

# 14. Initialize the flask restful(15 in resource.py)
api = Api(app)

class AppResource(Resource):
    def get(self):
        return "Welcome to the realestate apis"



# 18. Comment our the previous route and write one that incorporates the flask RESTful that
#  we just installed 
# api.add_resource(AppResource, '/')

# # 20 this accepts the methods ie GET  (19 in resource)
api.add_resource(Location,'/location', '/location/<int:id>')

 
