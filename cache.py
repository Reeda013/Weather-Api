import json
import os
from datetime import timedelta, datetime


cache_file = os.path.join(os.path.dirname(__file__), "cache.json")

cache_duration = timedelta(minutes=30)

def load_cache():
    if not os.path.exists(cache_file):
        return {}
    with open(cache_file, "r") as file:
        return json.load(file)


def save_cache(data):
    with open(cache_file, "w") as file:
        json.dump(data, file, indent=4) 


def get_cached_data(city):
    cache = load_cache()
    if city in cache:
        if cache[city]:
            time = datetime.fromisoformat(cache[city]["timestamp"])
            if datetime.now() - time < cache_duration:
                return cache[city]["weather"]
    return None


def cache_data(city, weather):
    cache = load_cache()
    cache[city] = {
        "weather": weather,
        "timestamp": datetime.now().isoformat()
    }

    save_cache(cache)