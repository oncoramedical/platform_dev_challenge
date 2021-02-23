import logging
import os
from datetime import datetime

from flask import jsonify, request
from flask_restful import Resource
from pymongo import DESCENDING, MongoClient
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)

mongo_url = os.getenv("MONGODB_URL")


class Prescription(Resource):
    def get(self, case_id):
        """
        Get the latest prescription for a given case

        Returns mongo document as json
        ---
        tags:
          - prescription
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
            400:
                description: Bad Request - invalid request params
            401:
                description: Unauthorized - user does not have permission to view prescription
            404:
                description: No prescription found
            503:
                description: Service Unavailable - connection to the database failed
        """
        case_id = int(case_id)

        client = MongoClient(mongo_url)
        db = client.get_database()

        # Get most recent prescription object
        prescription = db.prescriptions.find_one(
            {"case_id": case_id}, sort=[("timestamp", DESCENDING)]
        )

        return jsonify(prescription)

    def post(self, case_id):
        """
        Submit a prescription for predictions

        Saves the given prescription with a timestamp and returns the resulting ID and a full prediction object
        ---
        tags:
          - prescription
        parameters:
          - in: path
            name: case_id
            description: Case ID
            required: true
            type: integer
            x-example: 1
          - in: body
            name: prescription
            description: new prescription
            required: true
            schema:
                $ref: '#/definitions/Prescription'
        responses:
            200:
                description: OK
                schema:
                    type: object
                    properties:
                        prescription_id:
                            type: string
                        risk_prediction:
                            $ref: '#/definitions/RiskPrediction'
            400:
                description: Bad Request - invalid request params
            401:
                description: Unauthorized - user does not have permission to create plans
            500:
                description: Internal Server Error - analytics service failed
            503:
                description: Service Unavailable - connection to the database failed
        """
        case_id = int(case_id)
        prescription_doc = request.get_json()

        prescription_doc["timestamp"] = datetime.now()
        prescription_doc["case_id"] = case_id

        client = MongoClient(mongo_url)
        db = client.get_database()

        try:
            result = db.prescriptions.insert_one(prescription_doc)

            if result.acknowledged:
                prescription_id = result.inserted_id
                logger.info(
                    "Prescription successfully saved",
                    extra={"case_id": case_id, "prescription_id": prescription_id},
                )
                return jsonify({"prescription_id": prescription_id})
            else:
                logger.error("Prescription failed to save for unknown reason")
        except PyMongoError:
            logger.exception("Prescription failed to save")
