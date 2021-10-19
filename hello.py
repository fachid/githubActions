"""
high level support for doing this and that.
"""
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
    """
    A dummy docstring.
    """    
    app.run()

