import os
import random
from datetime import datetime

from flask.json import jsonify
from flask_restful import Resource
from pymongo import DESCENDING, MongoClient

mongo_url = os.getenv("MONGODB_URL")


class RiskPrediction(Resource):
    def get(self, case_id):
        """
        Get risk prediction for GI hospitalization risk.

        Returns a dictionary with the probability of hospitalization and model version
        ---
        tags:
          - risk_prediction
        parameters:
          - in: path
            name: case_id
            description: Case ID
            required: true
            type: integer
            x-example: 1
        responses:
          200:
            description: OK
            schema:
              type: object
              properties:
                prediction:
                  type: float
                version:
                  type: string
                created_at:
                  type: string
                  format: date-time
          204:
            description: The request is valid, but no predictions were generated
          400:
            description: Bad Request - invalid request params
        """
        case_id = int(case_id)

        client = MongoClient(mongo_url)
        db = client.get_database()

        # Get the relevant case document
        case = db.cases.find_one({"_id": case_id})

        # Get the most recent prescription for this case
        prescription = db.prescriptions.find_one(
            {"case_id": case_id}, sort=[("timestamp", DESCENDING)]
        )

        # Pretend there's some logic here to derive a risk prediction from the above case and prescription
        result = {"prediction": random.random(), "version": "1", "created_at": datetime.now()}

        return jsonify(result)
