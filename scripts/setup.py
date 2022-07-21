#!/usr/bin/env python3

from sqlalchemy import MetaData, create_engine
from flask_sqlalchemy import SQLAlchemy
from decouple import config


db = SQLAlchemy()
metadata = MetaData()
DB_TYPE = config('dbt')
DB_NAME = config("db")


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))


if DB_TYPE == "mysql":
    engine = create_engine('mysql://'+config('dbc')+"/"+DB_NAME)
else:
    # sqlite
    engine = create_engine('sqlite:///'+DB_NAME+".db")

metadata.create_all(engine)
