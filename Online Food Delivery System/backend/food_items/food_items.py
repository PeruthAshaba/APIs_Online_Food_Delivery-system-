from backend.db import db

class FoodItem(db.Model):
    __tablename__='food_items'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True)
    price = db.Column(db.String(255))  
    price_unit = db.Column(db.String(10),default='UGX')
    image = db.Column(db.String(200))
    stock = db.Column(db.Integer)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    order = db.relationship("Order",backref="food_item")



    def __init__(self,name,price,price_unit,image,stock,category_id):
        self.name=name
        self.price=price
        self.price_unit=price_unit
        self.image=image
        self.stock=stock
        self.category_id=category_id


        def __repr__(self):
            return f"<FoodItem {self.name} >"
    