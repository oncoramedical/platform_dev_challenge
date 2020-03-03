MODEL_TARGET_FIELD = "model_target"
MODEL_OUTCOME_FIELD = "model_outcome"
PREDICTIONS_FIELD = "predictions"
PRESCRIPTION_FIELD = "prescription"
PRESCRIPTION_ID_FIELD = "prescription_id"
TARGET_OBJECTIVES_FIELD = "target_objectives"


prescription_post_schema = {
    "type": "object",
    "required": [PRESCRIPTION_FIELD],
    "properties": {
        PRESCRIPTION_FIELD: {
            "type": "object",
            "required": [TARGET_OBJECTIVES_FIELD, MODEL_TARGET_FIELD, MODEL_OUTCOME_FIELD],
            "properties": {
                TARGET_OBJECTIVES_FIELD: {"type": "array", "items": {"type": "object"}},
                MODEL_TARGET_FIELD: {"type": "string"},
                MODEL_OUTCOME_FIELD: {"type": "string"},
            },
        }
    },
}
