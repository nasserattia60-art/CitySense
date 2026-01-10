from groq import Groq
from django.conf import settings
import json
from jsonschema import validate
from .prompt import SYSTEM_PROMPT
from .schema import analysis_schema

client = Groq(api_key=settings.GROQ_API_KEY)

def analyze_location_ai(address, lat, lng):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Location: {address}, Latitude: {lat}, Longitude: {lng}"
            }
        ],
        temperature=0.3
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)

    validate(instance=data, schema=analysis_schema)

    return data