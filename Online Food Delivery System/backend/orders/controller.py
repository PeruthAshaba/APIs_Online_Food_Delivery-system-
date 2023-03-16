#importing librries
from flask import jsonify,request,Blueprint
from backend.orders.orders import Order
from backend.db import db

#creating blueprint for orders
all_orders = Blueprint('orders', __name__, url_prefix='/orders')

#get all addresses
@all_orders.route("/")
def orders():
    orders=Order.query.all()
    results=[{ "quantity":order.quantity, "location":order.location, "user_id":order.user_id, "food_item_id":order.food_item_id, "status":order.status}for order in orders]
    return {"count":len(orders), "orders":results}

#creating new orders
@all_orders.route('/create', methods=['POST'])
def create_new_order():
    
    quantity=request.json['quantity']
    location=request.json['location']
    user_id=request.json['user_id']
    food_item_id=request.json['food_item_id']
    status=request.json['status']

    #validations

    if not quantity:
        return jsonify({'message':"order quantity is required"})
    if not location:
        return jsonify({'message':"your location is required"})
    if not user_id:
        return jsonify({'message':"user_id is required"})
    if not food_item_id:
        return jsonify({'message':"food_item_id is required"})
    if not status:
        return jsonify({'message':"status is required"})
    

    #storing the order data
    new_order=Order( quantity=quantity, location=location, user_id=user_id, food_item_id=food_item_id,status=status)

    #inserting values
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'Success':True,'Message':'You have successfully registered','data':new_order}),201


 #get order by id
@all_orders.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    db.session.add(order)
    db.session.commit()
    return jsonify({'message':'successful'})

#delete from the table
@all_orders.route('/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    order= Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': f'{order.name} order successfully deleted.'})

#update the order table
@all_orders.route('/update/<int:id>', methods=['PATCH'])
def update_order(id):
    order = Order.query.get_or_404(id)
    #data
    order.name=request.json['name']
    #add the updated data
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": f"{order.name}  order updated successfully"})

    







