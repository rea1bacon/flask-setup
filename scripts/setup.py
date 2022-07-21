#!/usr/bin/env python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from decouple import config
import pathlib

app = Flask(__name__)

DB_TYPE = config('dbt')
DB_NAME = config("db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if DB_TYPE == "mysql":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + \
        config('dbc')+"/"+DB_NAME
else:
    # sqlite
    path = str(pathlib.Path().resolve())
    print(path)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        path+'/src/app/'+DB_NAME+".db"

db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    message = db.Column(db.String(200))


print("[+] Creating database...")
db.create_all(app=app)
print("[+] Database created !")
print("[+] Adding one test row...")
TestMessage = Test(
    title="Great !", message="If you see this, you have completed the installation and everything is working fine")
db.session.add(TestMessage)
db.session.commit()
print("[+] Row commited !")
print("Start server with src/main.py")
