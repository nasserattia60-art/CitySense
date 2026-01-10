analysis_schema = {
    "type": "object",
    "properties": {
        "safety_score": {"type": "number"},
        "noise_level": {"type": "string"},
        "rent_level": {"type": "string"},
        "water_quality": {"type": "string"},
        "ai_score": {"type": "number"},
        "summary": {"type": "string"},
    },
    "required": [
        "safety_score",
        "noise_level",
        "rent_level",
        "water_quality",
        "ai_score",
        "summary",
    ]
}