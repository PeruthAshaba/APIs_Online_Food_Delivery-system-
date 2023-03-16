from backend.db import db


#creating the instance of the class
class District(db.Model):
    __tablename__='districts'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True)
    region_id = db.Column(db.Integer,db.ForeignKey('regions.id'))
    address = db.relationship("Address",backref="district")
    


#defining the function
    def __init__(self, region_id, name):
     self.region_id = region_id
     self.name = name

    
#function representation
#This returns what you want to see when the function is evoked
    def __repr__(self):
        return f"<District {self.name} >"