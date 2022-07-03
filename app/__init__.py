from flask import Flask


def StartApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "7893ad3dcb6fd0ec792b8530763a6a99"  # To change
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app
