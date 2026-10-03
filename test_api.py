import json
import urllib.request

payload = {
    "recipient": "Test Student",
    "achievement": "First Prize",
    "event": "AI Hackathon",
    "date": "2026-10-03"
}

request = urllib.request.Request(
    "http://127.0.0.1:5000/api/generate",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urllib.request.urlopen(request) as response:
    result = json.load(response)
    assert result["success"] is True
    print("API test passed:", result["certificate"]["certificate_id"])
