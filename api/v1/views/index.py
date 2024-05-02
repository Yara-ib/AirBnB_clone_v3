#!/usr/bin/python3
""" Index Module """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def route_status():
    """
    checking "status" Route
    Returns: JSON: "status": "OK"
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def route_stats():
    """"""    """
    Handling "stats" Route
    Returns: Count for each class object
    """
    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    })
