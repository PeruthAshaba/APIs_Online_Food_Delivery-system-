from backend.db import db

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50))  
    contact = db.Column(db.String(200))
    user_type = db.Column(db.String(100))
    password = db.Column(db.String(10))
    address = db.Column(db.String(255))

    address = db.relationship("Address",backref="user")
    order= db.relationship("Order",backref="user")

    def __init__(self, name, email,contact,user_type,password,address):
      self.name = name
      self.email = email
      self.contact = contact
      self.user_type = user_type
      self.password = password
      self.address=address


  


    def __repr__(self):
        return f"<User {self.name} >"
  

        
   #save a new instance
    def save(self):
        db.session.add(self)
        db.session.commit()

   #delete the item
    def delete(self):
        db.session.delete(self)
        db.session.commit()