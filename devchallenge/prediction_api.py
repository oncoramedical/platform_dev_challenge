import json
import logging
from unittest.mock import MagicMock

import requests

logger = logging.getLogger(__name__)


def get_risk_prediction(url: str, body: str) -> requests.Response:
    """
    Get risk prediction for gi hospitalization risk.

    Returns a dictionary with the probability of hospitalization and model version
    ---
    tags:
      - risk_prediction
    parameters:
      - in: body
        name: target_objectives
        description: target objectives from a prescription
        type: array
        required: true
        schema:
            $ref: '#/definitions/TargetObjectives'
      - in: body
        name: case
        description: individual case
        required: true
        schema:
            $ref: '#/definitions/Case'
      - in: body
        name: model_target
        required: true
        type: string
      - in: body
        name: model_outcome
        required: true
        type: string
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
    response = MagicMock()
    response.status_code = 200

    response_content = {'foo': 'bar'}
    response.json.return_value = response_content
    response.text = json.dumps(response_content)

    return response
