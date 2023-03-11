from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return {'HELLO': 'world'}

api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)