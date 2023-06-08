from flask import jsonify, render_template, request
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
        res = request.get_json()['res']
        
        if(res['action'] == 0):
            res['now_pos'], res['direction'] = go_forward(res['now_pos'], res['direction'])
        elif(res['action'] == 1):
            res['direction'] = turn_left(res['direction'])
        elif(res['action'] == 2):
            res['direction'] = turn_right(res['direction'])
        
        return jsonify(res = res)
