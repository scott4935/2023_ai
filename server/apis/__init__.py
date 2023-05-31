from .wumpus import Wumpus
def load_api(api_module):
    api_module.add_resource(Wumpus,'/wumpus',endpoint='wumpus')