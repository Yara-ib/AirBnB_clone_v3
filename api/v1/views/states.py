#!/usr/bin/python3
""" States Module """
from api.v1.views import app_views
from flask import abort, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def get_state():
    """
    Getting State objects
    Returns: list of all State objects
    """
    for item in storage.all(State):
        return item.to_dict()


@app_views.route('/states/<int: state_id>', strict_slashes=False)
def get_state_id(state_id):
    """
    Getting State object by id
    Returns: object | 404 if not found
    """
    if state_id not in storage.all(State):
        abort(404)
    else:
        for item in storage.all(State).values():
            if item.id == state_id:
                return item


@app_views.route('/states/<int: state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """
    Deleting State object by id
    Returns: Empty dictionary + '200': Ok | '404'
    """
    for item in storage.all(State).values():
        if item.id == state_id:
            del item
            return {}, 200
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    Creating new State object
    Returns: new object data + '201': created | '400'
    """
    json_data = request.get_json()
    if not json_data:
        abort(400, description='Not a JSON')
    elif not json_data['name']:
        abort(400, description='Missing name')
    else:
        return json_data, 201


@app_views.route('/states/<int: state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """
    Updating State object by id
    Returns: '200': ok | '404'
    """
    abort(404)
