import os

#base class
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass

#sub class of the base class
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:''@localhost/online_food_delivery_system'

class TestingConfig(Config):
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("TEST_DATABASE_URI")

#configuration object
config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig

}