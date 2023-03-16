from backend.db import db;


class Region(db.Model):
    __tablename__="regions"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True)
    district = db.relationship("District",backref="region")
  


 



    def __init__(self,name):
        self.name=name
    


        def __repr__(self):
            return f"<Region {self.name} >"

