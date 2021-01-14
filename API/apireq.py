import requests
import json

resp=requests.get("http://api.open-notify.org/astros.json")
print(resp.status_code)
data=resp.json()

print(resp.json())



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
    jsonstring= json.loads(text)
    print(jsonstring)

jprint(resp.json())