from flask import jsonify, render_template, request
from flask_restx import Namespace, Resource
from ..service.wumpus_service_bck import (
    turn_left, turn_right, go_forward, grab, shoot, climb, mk_map, new_setting, exec_agent
)

api = Namespace('wumpus', description='Wumpus related operations')

@api.route('/')
class Wumpus(Resource):
    def get(self):
        print("test")
        res = new_setting()

        return jsonify(res = res)

    def post(self):
        res = request.get_json()['res']
        res = exec_agent(res)
        
        return jsonify(res = res)
