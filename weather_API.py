import requests
import json

hdr = {"X-API-Key": "YOUR_API_KEY"}
req = requests.get("https://api.checkwx.com/metar/kjfk/decoded", headers=hdr)

print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)

    