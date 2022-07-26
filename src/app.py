from dotenv import load_dotenv
from flask import Flask
from database import database
from decouple import config
from flask_restful import Api
from flask_cors import CORS

from apps.FrontEnd.views.Home import Home
from apps.Api.Apiendpoints import Testapi


def StartApp():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    database.init_app(app)
    app.register_blueprint(Home, url_prefix='/')
    api = Api(app)
    api.add_resource(Testapi, '/v1/test', subdomain='api')
    cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})
    return app


# Get env variable
load_dotenv()

if __name__ == '__main__':
    app = StartApp()
    app.run(host="localhost", port=5000)
