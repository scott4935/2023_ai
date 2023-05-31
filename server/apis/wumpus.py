from flask import jsonify
from flask_restx import Namespace, Resource
from ..service.wumpus_service import (
    KB, turn_left, turn_right, go_forward, grab, shoot, climb, mk_map, new_setting
)

api = Namespace('wumpus', description='Wumpus related operations')

@api.route('/')
class Wumpus(Resource):
    def get(self):
        print("test")
        res = new_setting()
        print(res['now_pos'])
        print(res['agent_map'])
        return jsonify(res = res)

    def post(self):
        print("tesT")
        return "post test"

class Test(Resource):
    def get(self):
        print("test")
        return "test get test"

    def post(self):
        print("tesT")
        return "test post test"