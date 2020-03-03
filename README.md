# Overview

Oncora has a concept of `case` objects that represent a single course of radiation treatment. Users may associate one or more `prescription` objects with a given `case`.

This project contains an API to store and retrieve those `prescription` objects, defined in `api.py`. It exposes a single endpoint, which accepts two methods:

| Endpoint                  | Method | Description                                                                  |
| ------------------------- | ------ | ---------------------------------------------------------------------------- |
| `/prescription/<case_id>` | `GET`  | Get the latest prescription for a given case                                 |
| `/prescription/<case_id>` | `POST` | Submit a prescription to associate with a case and retrieve risk predictions |

Oncora also has a separate API that can be used to retrieve a set of "risk predictions" for a given `case` and `prescription`. This is mocked by a function in `prediction_api.py`.

# Goals

1. When a user submits a prescription to be saved, use the prediction api to retrieve predictions, store them in a database along with the `prescription` and `case` used to generate them, and include the predictions in the response to the client.
   - The predictions should be stored in a mongo collection called `predictions`
1. Add a suite of unit tests
   - A single, failing test already exists
   - Refactor the existing code as much as you like to accomplish this

# Setup

1. [Install pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) if it isn't already installed.
1. Clone this repo
1. Create virtual environment and install dependencies: `PIPENV_VENV_IN_PROJECT=1 pipenv install -d`
1. Open the project in VS Code and run the test suite, or `pipenv run pytest`
