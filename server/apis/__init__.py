from .wumpus import Wumpus, Test

def load_api(api_module):
    api_module.add_resource(Wumpus,'/wumpus',endpoint='wumpus')
    api_module.add_resource(Test,'/test',endpoint='test')