from flask_restful import reqparse, Resource
from ..service.wumpus_service import *

class Wumpus(Resource):
    def get(self):
        return "get test"
    def post(self):
        return "post test"
