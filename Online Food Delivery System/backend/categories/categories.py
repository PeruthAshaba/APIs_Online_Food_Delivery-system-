from backend.db import db

#creating the instance of the class
class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    food_item = db.relationship("FoodItem",backref="category")




#defining the function 
def __init__(self,name):
    self.name=name

    
   



#function representation
#This returns what you want to see when the function is evoked
def __repr__(self):
    return f"<Category {self.name} >"
