import redis
import json
import time
import os
import re

r = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)


def normalize_query(query):
    query = query.lower().strip()
    query = re.sub(r'[^\w\s]', '', query)
    query = " ".join(query.split())
    return query

def get_cache(key):
    key = normalize_query(key)
    print(f"GET CACHE: {key}")
    data = r.get(key)

    if not data:
        print("CACHE MISS")
        return None
    print("CACHE HIT")
    try:
        payload = json.loads(data)
        return payload["value"]   # ✅ FIXED
    except:
        return data
    

def set_cache(key, value, ttl=3600):
    key = normalize_query(key)
    print(f"SET CACHE: {key}")
    payload = {
        "value": value
    }

    r.setex(key, ttl, json.dumps(payload))