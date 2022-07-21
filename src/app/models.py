from . import db


class Test(db.Model):
    """
    Test table, remove it
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    message = db.Column(db.String(200))
