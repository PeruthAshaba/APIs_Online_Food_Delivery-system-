#importing library
from flask import jsonify, request, Blueprint
from backend.districts.districts import District
from backend.db import db
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required


all_districts = Blueprint('districts',__name__,url_prefix='/districts')
#get all districts
@all_districts.route("/")
def districts():
    districts = District.query.all()
    results=[{ "name":district.name,"region_id":district.region_id }for district in districts]
    return jsonify({"count":len(districts), "districts":results})


#creating districts
# @jwt_required()
@all_districts.route('/create',methods=['POST'])
def create_new_district():
    name=request.json['name']
    region_id=request.json['region_id']
    



    #validations
    if not name:
        return jsonify({'error':"Disrtict name is required"}),400
    
    if not region_id:
        return jsonify({'error':"District region name is required"}),400
    
    if District.query.filter_by(name=name).first():
        return jsonify({'error':"District name exists"}),409
    
    new_district=District(name=name,region_id=region_id)

    #inserting values
    db.session.add(new_district)
    db.session.commit()
    return jsonify({'message':'You have sucessfully created a new district','data':new_district}),201


 #get district by id
@all_districts.route('/districts/<int:id>', methods=['GET'])
def get_district(id):
    district = District.query.get_or_404(id)
    db.session.add(district)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_districts.route('/delete/<int:id>', methods=['DELETE'])
def delete_district(id):
    district = District.query.get_or_404(id)
    db.session.delete(district)
    db.session.commit()
    return jsonify({'message': f'{district.name} user successfully deleted.'})

#update the districts table
@all_districts.route('/update/<int:id>', methods=['PATCH'])
def update_district(id):
    district = District.query.get_or_404(id)
    #data
    district.name=request.json['name']
    #add the updated data
    db.session.add(district)
    db.session.commit()
    return jsonify({"message": f"{district.name}  district updated successfully"})
