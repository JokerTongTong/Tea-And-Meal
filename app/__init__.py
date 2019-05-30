from flask import Flask
from flask_restful import Api
from  flask_cors import CORS
from app import resource

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key = "A0Zr98j/3yX R~XHH!jmNJLWX/,?RT"
    api = Api(app)
    api.add_resource(resource.Helloworld,"/")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()