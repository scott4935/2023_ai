from flask import jsonify, render_template
from flask_restx import Namespace, Resource
from ..service.wumpus_service import (
    KB, turn_left, turn_right, go_forward, grab, shoot, climb, mk_map, new_setting
)

api = Namespace('test', description='Wumpus related operations')

@api.route('/')
class Test(Resource):
    def get(self):
        return render_template('test.html')

    def post(self):
        print("tesT")
        return "test post test"