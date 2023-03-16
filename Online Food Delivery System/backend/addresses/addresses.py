from backend.db import db

#creating the instance of the class
class Address(db.Model):
    __tablename__='addresses'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    district_id=db.Column(db.Integer,db.ForeignKey('districts.id'))

#defining the function 
def __init__(self,id,name,user_id,district_id):
    self.id=id
    self.name=name
    self.user_id=user_id
    self.district_id=district_id
    



#function representation
#This returns what you want to see when the function is evoked
def __repr__(self):
    return f"<Address {self.name} >"