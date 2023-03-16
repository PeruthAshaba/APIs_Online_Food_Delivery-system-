from flask import jsonify,request,Blueprint
from backend.db import db
from backend.food_items.food_items import FoodItem

all_food_items = Blueprint('food_items',__name__,url_prefix='/food_items')

@all_food_items.route("/")
def food_iteoms():
    food_items=FoodItem.query.all()
    results=[{ "name":food_item.name,"price":food_item.price, "price_unit":food_item.price_unit,"image":food_item.image,"stock":food_item.stock,"category_id":food_item.category_id}for food_item in food_items]
    return jsonify({"count":len(food_items), "food_items":results}) 


#creating food_items
@all_food_items.route('/create', methods=['POST'])
def create_food_item():
    name=request.json['name']
    price=request.json['price']
    price_unit=request.json['price_unit']
    image=request.json['image']
    stock=request.json['stock']
    category_id=request.json['category_id']


    #validations
    if not name:
        return jsonify({'error':"FoodItem name is required"})
    if not price:
        return jsonify({'error':"FoodItem price is required"})
    if not price_unit:
        return jsonify({'error':"FoodItem price_unit is required"})
    if not stock:
        return jsonify({'error':"FoodItem stock is required"})
    if not category_id:
        return jsonify({'error':"Food category name is required"})
    if FoodItem.query.filter_by(name=name).first() is not None:
        return jsonify({'error':"FoodItem name exist"}),409
    
    food_item=FoodItem(name=name,price=price,price_unit=price_unit,stock=stock,image=image,category_id=category_id)

    #inserting values
    db.session.add(food_item)
    db.session.commit()
    return jsonify({'message':'You have successfully created a new food item','data':food_item}),201


 #get food_item by id
@all_food_items.route('/food_items/<int:id>', methods=['GET'])
def get_food_item(id):
    food_item = FoodItem.query.get_or_404(id)
    db.session.add(food_item)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_food_items.route('/delete/<int:id>', methods=['DELETE'])
def delete_food_item(id):
    food_item = FoodItem.query.get_or_404(id)
    db.session.delete(food_item)
    db.session.commit()
    return jsonify({'message': f'{food_item.name} category successfully deleted.'})

#update table
@all_food_items.route('/update/<int:id>', methods=['PATCH'])
def update_category(id):
    food_item = FoodItem.query.get_or_404(id)
    #data
    food_item.name=request.json['name']
    #add the updated data
    db.session.add(food_item)
    db.session.commit()
    return jsonify({"message": f"{food_item.name}  food_item updated successfully"})

