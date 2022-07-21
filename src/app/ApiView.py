from flask import Blueprint
import flask
from .models import Test

Api = Blueprint('api', __name__)


@Api.route('/v1/test')
def test():
    try:
        testobj = Test.query.first()
        resp = {"type": "success", "slug": testobj.title, "msg": testobj.message}
        return resp
    except Exception as e:
        return {"type": "failure", "slug": "Something failed during the process...", "msg": str(e)}
