from flask import Flask, render_template
from flask_restx import Api, Resource
from server.apis import load_api

app = Flask(__name__)
myApi=Api(app, errors=Flask.errorhandler)

@app.route("/")
@app.route("/index")
def index():
    return "hello world!" 
    #return render_template("index.html")

load_api(myApi)
if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5000, debug=True)