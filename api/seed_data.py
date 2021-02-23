import logging
import os
from datetime import datetime

from pymongo import MongoClient

logger = logging.getLogger(__name__)

mongo_url = os.getenv("MONGODB_URL")


def seed_data():
    client = MongoClient(mongo_url)
    db = client.get_database()

    logger.info("Clearing existing cases and prescriptions")
    db.cases.delete_many({})
    db.prescriptions.delete_many({})

    logger.info("Adding seed data")

    db.cases.insert_one(
        {"_id": 123, "case_id": 123, "patient": {"first_name": "John", "last_name": "Smith"}}
    )

    db.prescriptions.insert_one(
        {
            "_id": 1,
            "case_id": 123,
            "timestamp": datetime.now(),
            "targetObjectives": [
                {
                    "targets": ["lung_left"],
                    "fraction_set": "Initial",
                    "technique": "IMRT",
                    "dose": 60.0,
                    "fractions": 30,
                }
            ],
        }
    )


if __name__ == "__main__":
    seed_data()
