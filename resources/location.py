
#  we are creating this file so we can convert our location to a resource
#  then after that we add in fields and marshal with to handle serializing 
from flask_restful import Resource, fields, marshal_with, reqparse

from models import LocationModel, db

# after importing fileds and marshal_with we define our resource fileds
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
}




# 21 Create location resource: (20 in app)
class Location(Resource):
    #  define parser  
    parser = reqparse.RequestParser()
    #  dedine the argument and required fields
    parser.add_argument("name", required=True, help="Location name is required")
       
    # get a single location
    #  then after defining resource_fields we add marshal_with
    @marshal_with(resource_fields)
    def get(self, id=None):
        # the above specifies that if the id is present we get a
        #  single location else we get all the locations

        # after adding marshal_with we add a condition ie to 
        #  check if the id exists we add in a single location

        if id:
            location = LocationModel.query.filter_by(id = id).first()
            return location
        else:
            # get alll location
            locations = LocationModel.query.all();
            return locations
        
    # Next define post method but first import reqparser then define parser
    def post(self):
        data = Location.parser.parse_args()

        # this step ie the two stars unpacks a dict and passes it as key-value pairs
        #  eg {"name": "Naivasha"} => name: Naivasha
        # technically it works like this; name=data['name']
        #  so instead we use the spread operator **
        location = LocationModel(**data)
        
    #  after creating the post method the last thing we do is to hook up
        #  our database to be able to persist data to it
        try:
            db.session.add(location)
            db.session.commit()

            return {"message": "Location created succesfully"}
        except:
            return {"message": "Unable to save location"}

        
    
   
