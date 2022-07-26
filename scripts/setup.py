#!/usr/bin/env python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from decouple import config
import pathlib

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
path = str(pathlib.Path().resolve())
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+path+"/src/db_dev.db"


db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    message = db.Column(db.String(200))


print("[+] Creating developement database...")
db.create_all(app=app)
print("[+] Database created !")
print("[+] Adding one test row...")
TestMessage = Test(
    title="Great !", message="If you see this, you have completed the installation and everything is working fine")
db.session.add(TestMessage)
db.session.commit()
print("[+] Row commited !")
print("Start server with src/app.py and access it to http://flaskezs.com:5000/")
