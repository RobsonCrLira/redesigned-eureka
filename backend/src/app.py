from flask import Flask, request
from flask_restful import Resource, Api
from search import Search
import json

app = Flask(__name__)
api = Api(app)


class searchDell(Resource):
    def get(self):
        response = Search.findProduct('https://www.dell.com/pt-br/search/i7')
        return response


api.add_resource(searchDell, '/find')

if __name__ == '__main__':
    app.run(debug=True)
