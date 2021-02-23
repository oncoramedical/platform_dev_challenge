from flask.json import jsonify
from flask_restful import Resource


class Status(Resource):
    def get(self):
        return jsonify({"status": "up"})
