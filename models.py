# 4. Import sqlalchemy
from flask_sqlalchemy import SQLAlchemy 

# 5. Initialize our db
db = SQLAlchemy()


# 6. create User model  (step 7 in app.py)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable= False)
    last_name = db.Column(db.Text, nullable= False)
    phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now()) #created automatically when something is added to database
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now()) # created automatically when something is updated in the database
    # implementing a soft delete feature
    # isDeleted = db.Column(db.Boolean, server_default=False)
    # or we can also write it like this 
    # deleted_at = db.Column(db.TIMESTAMP)


# 11. create location model (from 10 in app.py)
class LocationModel(db.Model):
    
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable= False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now()) 
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now())
    


#  12. Create Property model 
class PropertyModel(db.Model):

    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable= False)
    description = db.Column(db.String, nullable= False)
    listing_price = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, nullable=False)
    type_of_property = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now()) 
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now())
