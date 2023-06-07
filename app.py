from flask import Flask, jsonify
from flask_restx import Api, Resource
from flask_cors import CORS
from server.apis import load_api

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app,expose_headers='Location')
myApi=Api(app, errors=Flask.errorhandler)

@app.route("/", methods=['GET'])
def hello():
    return "hello world!" 


load_api(myApi)
if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5000, debug=True, use_reloader=False)