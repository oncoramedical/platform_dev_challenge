# Overview

Oncora has a concept of `case` objects that represent a single course of radiation treatment. Users may associate one or more `prescription` objects with a given `case`.

This project contains an API to store and retrieve those `prescription` objects, and to retrieve `risk_predictions` for a case based on its latest prescription. These are the available endpoints:

| Endpoint                  | Method | Description                                                                | Code                           |
| ------------------------- | ------ | -------------------------------------------------------------------------- | ------------------------------ |
| `/prescription/<case_id>` | `GET`  | Get the latest prescription for a given case                               | `resources/prescription.py`    |
| `/prescription/<case_id>` | `POST` | Submit a prescription to associate with a case                             | `resources/prescription.py`    |
| `/prediction/<case_id>`   | `GET`  | Retrieve risk predictions for a case based on its most recent prescription | `resources/risk_prediction.py` |

All data is stored in MongoDB. Case documents are stored in the `case` collection, and prescription documents are stored in the `prescription` collection.

# Goals

1. When a user submits a prescription to be saved we want to go ahead and generate risk predictions for that prescription, store them in the database along with the `prescription` and `case` used to generate them, and include the predictions in the response to the client.
   - The predictions should be stored in a collection called `predictions`
   - The predictions should be returned from the API as an attribute named `risk_prediction`
2. Add unit tests to cover any modified code, or any other appropriate test cases you happen to find
   - Refactor the existing code as much as you like to accomplish this

# Setup

1. [Install pipenv](https://pipenv.pypa.io/en/latest/installation.html) if it isn't already installed.
2. Clone this repo
3. Create virtual environment and install dependencies: `PIPENV_VENV_IN_PROJECT=1 pipenv install -d`
   - Pipenv will create a virtual environment in the project directory, so when
4. Start the API: `docker-compose up -d`
   - This will run a REST API listening on port 5000 and a MongoDB instance listening on port 27017.
5. Add some initial seed data to the database: `docker-compose exec api python -m seed_data`
   - Use this same command anytime to replace any data added to the database during development/testing with the seed data
6. Open the project in your editor of choice
   - Note that this project already includes some configuration to simplify debugging in VS Code, but you're welcome to use whatever editor/environment you like

# Testing

1. The automated tests can be run with pytest: `pipenv run pytest`
   - You should initially see one passing and one failing test
   - Feel free to use any testing tools in your editor, too. If using VS Code, this should already work
2. Some sample api requests are included in two formats:
   1. `sample_requests.curl.sh` has a few curl commands
   2. `sample_requests.postman_collection.json` has the same requests as a collection that you can import into Postman