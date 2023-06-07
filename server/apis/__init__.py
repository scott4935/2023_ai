from .wumpus import Wumpus
from .test import Test

def load_api(api_module):
    api_module.add_resource(Wumpus,'/wumpus',endpoint='wumpus')
    api_module.add_resource(Test,'/test',endpoint='test')