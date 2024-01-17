
#  we are creating this file so we can convert our location to a resource
from flask_restful import Resource

from models import LocationModel


# 21 Create location resource: (20 in app)
class Location(Resource):
    # get a single location
    def get(self, id):
        location = LocationModel.query.filter_by(id = id).first()
        # print(location.json())
        return " a single location"
    
    def put(self, id):
        print(f"Updating {id}")
        return "Location update"
        
    def delete(self, id):
        print(f"Deleting {id}")
        return 

