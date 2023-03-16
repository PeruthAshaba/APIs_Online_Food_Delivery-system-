from flask import  jsonify, request, Blueprint
from backend.regions.regions import Region
from backend.db import db
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required


#creating Blueprints
all_regions = Blueprint('regions', __name__, url_prefix='/regions')


@all_regions.route("/")
def regions():
    regions=Region.query.all()
    results=[{ "name":region.name}for region in regions]
    return {"count":len(regions), "regions":results}
    
      
    


#creating regions
# @jwt_required()
@all_regions.route('/create', methods= ['POST'])
def new_region():
    name=request.json['name']

    # created_by=get_jwt_identity()

      
  
    #validations
    if not name:
        return jsonify({'error':"Region name is required"}),400
    
    if not id:
        return jsonify({'error':"Region id is required"}),400
    
    

    if Region.query.filter_by(name=name).first():
        return jsonify({'error': "Region name exists"}), 409 

    #storing the constraints
    new_region = Region(name=name) 
      
    #inserting values
    db.session.add( new_region)
    db.session.commit()
    return jsonify({'message':'New region created sucessfully','data': new_region}),201



 #get region by id
@all_regions.route('/regions/<int:id>', methods=['GET'])
def get_region(id):
    region = Region.query.get_or_404(id)
    db.session.add(region)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_regions.route('/delete/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get_or_404(id)
    db.session.delete(region)
    db.session.commit()
    return jsonify({'message': f'{region.name} region successfully deleted.'})

#update the regions table
@all_regions.route('/update/<int:id>', methods=['PATCH'])
def update_region(id):
    region = Region.query.get_or_404(id)
    #data
    region.name=request.json['name']
    #add the updated data
    db.session.add(region)
    db.session.commit()
    return jsonify({"message": f"{region.name}  region updated successfully"})






        



  
                           




    






