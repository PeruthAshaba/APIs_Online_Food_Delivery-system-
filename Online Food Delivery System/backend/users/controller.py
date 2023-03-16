#registering a new user
from flask import jsonify,request,Blueprint
from backend.db import db
from backend.users.users import User


all_users=Blueprint('users',__name__,url_prefix='/users')
#get all users
@all_users.route("/")
def regions():
    users = User.query.all()
    results=[{ "name":user.name, "email":user.email, "contact":user.contact, "password":user.password, "address":user.address}for user in users]
    return {"count":len(users), "users":results}
    
#creating new users
@all_users.route('/create',methods=['POST'])
def new_user():
    name=request.json['name']
    email=request.json['email']   
    contact=request.json['contact']
    user_type=request.json['user_type'] 
    password=request.json['password'] 
    address=request.json['address']



    #validations

    if not name:
        return jsonify({"message":"Your name is required"}),400
    
    if not email:
        return jsonify({"message":"Your email address is required"}),400
    if not contact:
        return jsonify({"message":"Your contact is required"}),400
    if not password:
        return jsonify({"message":"Your password is required "}),400
    if len(password)<6:
        return jsonify({"message":"Password should be longer than 6 characters"}),400
    
    if not address:
        return jsonify({"message":"Your address is required"}),400
    if not user_type:
        return jsonify({"message":"Your user_type is required"}),400
    if User.query.filter_by(name=name).first():
        return jsonify({'error': "User name exists"}), 409 
    
    #storing the user data
    new_user = User(name=name,email=email,contact=contact,user_type=user_type,password=password,address=address)

    #inserting values
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success':True,'message':'You have successfully created a new user','data':new_user}),201


 #get user by id
@all_users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_users.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'{user.name} user successfully deleted.'})

#update the users table
@all_users.route('/update/<int:id>', methods=['PATCH'])
def update_user(id):
    user = User.query.get_or_404(id)
    #data
    user.name=request.json['name']
    #add the updated data
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": f"{user.name}  user updated successfully"})
    



