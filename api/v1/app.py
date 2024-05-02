#!/usr/bin/python3
""" App Module """
from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Handling closing the resource
    Returns: Nothing
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """
    Handling 404 page | Not found pages
    Returns: JSON: "error": "Not found"
    """
    return jsonify({'error': 'Not found'})


if __name__ == '__main__':
    """ Handling the connection when running flask app """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=int(port), threaded=True, debug=True)
