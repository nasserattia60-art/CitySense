REQUIRED_FIELDS = {
    "safety",
    "noise",
    "rent",
    "water",
    "population",
    "ai_score",
    "summary",
}

def validate_response(data: dict):
    if not REQUIRED_FIELDS.issubset(data.keys()):
        raise ValueError("Missing fields in AI response")

    for key in REQUIRED_FIELDS:
        if key == "summary":
            continue
        value = data[key]
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise ValueError(f"Invalid value for {key}")
