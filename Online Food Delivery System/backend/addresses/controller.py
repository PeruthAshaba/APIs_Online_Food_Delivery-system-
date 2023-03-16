#importing libraries
from flask import jsonify, request, Blueprint
from backend.addresses.addresses import Address
from backend.db import db


#creating a blueprint of addresses
#A blueprint is a group of our endpoints
all_addresses = Blueprint('addresses',__name__,url_prefix='/addresses')

#get all addresses
@all_addresses.route("/")
def addresses():
    addresses=Address.query.all()
    results=[{ "name":address.name, "district_id":address.district_id, "user_id":address.user_id}for address in addresses]
    return jsonify({"count":len(addresses), "addresses":results})



#We use CRUD
#create addresses
@all_addresses.route('/create', methods=['POST'])
def create_new_address():
    name=request.json['name']
    district_id=request.json['district_id']
    user_id=request.json['user_id']
  

    #we are validating the created addresses
    if not name:
        return jsonify({'error':"Address name is required"}),400
    
    if not district_id:
        return jsonify({'error':"District name is required"}),400
    

    
    if not user_id:
        return jsonify({'error':"User name is required"}),400
    

    # #checking for constraints
    # if Address.query.filter_by(user_id=user_id).first() is not None and Address.

    #storing the address data
    new_address=Address(name=name,district_id=district_id,user_id=user_id)

    #inserting values
    db.session.add(new_address)
    db.session.commit()
    return jsonify({'Success':True,'Message':'You have successfully registered','data':new_address}),201


 #get address by id
@all_addresses.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    address = Address.query.get_or_404(id)
    db.session.add(address)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_addresses.route('/delete/<int:id>', methods=['DELETE'])
def delete_address(id):
    address= Address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()
    return jsonify({'message': f'{address.name} address successfully deleted.'})

#update the address table
@all_addresses.route('/update/<int:id>', methods=['PATCH'])
def update_address(id):
    address = Address.query.get_or_404(id)
    #data
    address.name=request.json['name']
    address.district_id=request.json['district_id']
    address.user_id=request.json['user_id']

    #add the updated data
    db.session.add(address)
    db.session.commit()
    return jsonify({"message": f"{address.name}  address updated successfully", "message": f"{address.district_id} district_id updated successfully", "message": f"{address.user_id} user_id updated successfully" })


