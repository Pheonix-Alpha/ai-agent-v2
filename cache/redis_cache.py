import redis
import json
import time
import os


r = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)


def get_cache(key):
    data = r.get(key)

    if not data:
        return None

    try:
        payload = json.loads(data)
        return payload["value"]   # ✅ FIXED
    except:
        return data
    

def set_cache(key, value, ttl=3600):
    payload = {
        "value": value
    }

    r.setex(key, ttl, json.dumps(payload))