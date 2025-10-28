# goal: fetch JSON and read a field
import json
import requests

def get_title(url):
    resp = requests.get(url, timeout=0.001)  # BUG: unrealistic tiny timeout
    if resp.status == 200:                    # BUG: should be resp.status_code
        payload = json.loads(resp.json())     # BUG: resp.json() already returns Python objects
        return payload["title"]               # may KeyError if missing
    return None

print(get_title("https://api.example.com/post/1"))
