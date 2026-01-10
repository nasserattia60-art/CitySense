from apps.ai_engine.services.analyze import analyze_location
import geonamescache 
from rapidfuzz import process

def run_analysis(address: str) -> dict:
    """
    Calls AI engine and returns structured data
    """
    return analyze_location(address)



gc = geonamescache.GeonamesCache()
cities = gc.get_cities()
ALL_CITIES = [
    {
        "name": c["name"],
        "lat": c["latitude"],
        "lon": c["longitude"],
    }
    for c in cities.values()
]
CITY_BY_NAME = {c["name"]: c for c in ALL_CITIES}

def suggest_city_fuzzy(query, limit=10):
    names = CITY_BY_NAME.keys()
    matches = process.extract(query, names, limit=limit)
    return [CITY_BY_NAME[name] for name, score, _ in matches if score > 65]