from flask import jsonify, render_template, request
from flask_restx import Namespace, Resource
from ..service.wumpus_service import (
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
        
        if(res['action'] == 0):
            res['now_pos'], res['direction'], res['agent_map'] = go_forward(res['now_pos'], res['direction'])
            res['act_list'].append('go_forword')
        elif(res['action'] == 1):
            res['direction'] = turn_left(res['direction'])
            res['act_list'].append('turn_left')
        elif(res['action'] == 2):
            res['direction'] = turn_right(res['direction'])
            res['act_list'].append('turn_right')
        
        #exec_agent(res)
        
        return jsonify(res = res)
