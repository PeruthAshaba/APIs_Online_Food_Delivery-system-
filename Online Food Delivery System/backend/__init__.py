from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from backend.db import db


def create_app(config_name):#application factory function
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")



    db.init_app(app)
    #importing Blue print
    from backend.addresses.controller import all_addresses
    from backend.categories.controller import all_categories
    from backend.districts.controller import all_districts
    from backend.food_items.controller import all_food_items
    from backend.regions.controller import all_regions
    from backend.users.controller import all_users
    from backend.orders.controller import all_orders

    #registering blue prints for the routes to work
    app.register_blueprint(all_addresses)
    app.register_blueprint(all_categories)
    app.register_blueprint(all_districts)
    app.register_blueprint(all_food_items)
    app.register_blueprint(all_regions)
    app.register_blueprint(all_users)
    app.register_blueprint(all_orders)





    return app




    



