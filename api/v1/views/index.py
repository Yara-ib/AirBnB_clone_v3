#!/usr/bin/python3
""" Index Module """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def route_status():
    """
    Handling "status" Route
    Returns: JSON: "status": "OK"
    """
    return jsonify({'status': 'OK'})
