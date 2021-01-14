import requests
import json
 
parameters = {
    "lat": 40.71,
    "lon": -74
}

response=requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
data=response.json()
#print(response.json())


def jprint(obj):
    text=json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
#jprint(response.json())