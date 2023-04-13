import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Conexion a mongo
    # client = MongoClient(
    #     "localhost",
    #     int(os.getenv("MONGODB_PORT", 27017)),
    #     username=os.getenv("MONGODB_USER", "root"),
    #     password=os.getenv("MONGODB_PASSWORD", "root"),
    # )

    @app.route("/")
    def hello_world():
        return "Hola Maxi y Gustavo!"

    return app
