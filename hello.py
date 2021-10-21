from flask import Flask, request, send_from_directory
from flask import Response
from flask_restful import reqparse, abort, Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    """
    A dummy docstring.
    """
    print(request.headers)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
