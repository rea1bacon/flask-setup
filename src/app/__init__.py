from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from decouple import config

db = SQLAlchemy()
DB_TYPE = config('dbt')
DB_NAME = config("db")


def StartApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config("secret")
    if DB_TYPE == "mysql":
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://" + \
            config('dbc')+"/"+DB_NAME
    elif DB_TYPE == "sqlite":
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
            DB_NAME+".db"
    else:
        print("Error : unknown type of database :" + DB_TYPE)
    db.init_app(app)
    from .HomeView import Home
    app.register_blueprint(Home, url_prefix='/')
    from .models import Test

    CreateDB(app)

    return app


def CreateDB(app):
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all(app=app)
