__version__ = "0.1.0"

import os

from flask import Flask, jsonify
from flask_cors import CORS
from typing import Optional, Mapping, Any


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "server.sqlite"),
    )

    # enable CORS
    # TODO: this setup allows cross-origin requests on ALL routes. In
    # production, ONLY allow cross-origin requests from the domain where the
    # front-end application is hosted. Refer to the Flask-Cors documentation:
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app, resources={r"/*": {"origins": "*"}})

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello() -> str:
        return "Hello, World!"

    @app.route("/ping", methods=["GET"])
    def ping_pong():
        return jsonify("pong!")

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    from . import blog

    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    return app
