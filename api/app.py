import datetime
import json
import logging

from bson import ObjectId
from flask import Flask
from flask_restful import Api

from api.debug import setup_debugger
from api.resources import prescription, risk_prediction, status

logging.basicConfig(level=logging.DEBUG)
setup_debugger()


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        # Put datetime in pymongo serialized format
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


app = Flask("platform_dev_challenge")
app.json_encoder = CustomEncoder
api = Api(app)

api.add_resource(status.Status, "/status")
api.add_resource(prescription.Prescription, "/prescription/<case_id>")
api.add_resource(risk_prediction.RiskPrediction, "/prediction/<case_id>")
