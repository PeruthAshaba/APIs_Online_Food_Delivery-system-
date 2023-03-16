#importing libraries
from flask import jsonify, request, Blueprint
from backend.categories.categories import Category
from backend.db import db


all_categories=Blueprint('categories',__name__,url_prefix='/categories')

@all_categories.route("/")
def categories():
    categories=Category.query.all()
    results=[{ "name":category.name}for category in categories]
    return jsonify({"count":len(categories), "categories":results})


#creating categories
@all_categories.route('/create',methods=['POST'])
def new_food_category():
    name=request.json['name']
   
   
    


#validations
    if not name:
        return jsonify({'error':"Food category name is required"}),400
    # if name already exists,status code is 409
    if Category.query.filter_by(name=name).first():
        return jsonify({'error':"Food category name exists"}),409  
    
    #storing the category data
    new_food_category=Category(name=name)

    #inserting values
    db.session.add(new_food_category)
    db.session.commit()
    return jsonify({'success':True,'message':'You have successfully created a new food category','data':new_food_category}),201


 #get category by id
@all_categories.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_categories.route('/delete/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f'{category.name} category successfully deleted.'})

#update the category table
@all_categories.route('/update/<int:id>', methods=['PATCH'])
def update_category(id):
    category = Category.query.get_or_404(id)
    #data
    category.name=request.json['name']
    #add the updated data
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": f"{category.name}  category updated successfully"})