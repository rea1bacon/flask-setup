from flask_restful import Resource
from .models import Test


class Testapi(Resource):
    def get(self):
        try:
            testobj = Test.query.first()
            resp = {"type": "success", "slug": testobj.title,
                    "msg": testobj.message}
            return resp
        except Exception as e:
            return {"type": "failure", "slug": "Something failed during the process...", "msg": str(e)}
