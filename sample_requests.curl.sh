#!/bin/bash

# Status
curl --location --request GET 'http://localhost:5000/status'

# Get Prescription
curl --location --request GET 'http://localhost:5000/prescription/123'

# Post Prescription
curl --location --request POST 'http://localhost:5000/prescription/123' \
--header 'Content-Type: application/json' \
--data-raw '{
    "targetObjectives": [
        {
            "dose": 60.0,
            "fraction_set": "Initial",
            "fractions": 30,
            "targets": [
                "lung_right"
            ],
            "technique": "IMRT"
        }
    ]
}'

# Get Prediction
curl --location --request GET 'http://localhost:5000/prediction/123'
