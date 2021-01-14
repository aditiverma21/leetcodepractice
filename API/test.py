import requests

resp = requests.get("http://api.open-notify.org/astros.json")
print(resp.status_code)
print(resp.json())
data = resp.json()
print(data["people"][3])
'''

{
    'message': 'success', 
    'people': [
            {'name': 'Alexey Ovchinin', 'craft': 'ISS'},
            {'name': 'Nick Hague', 'craft': 'ISS'},
            {'name': 'Christina Koch', 'craft': 'ISS'},
            {'name': 'Alexander Skvortsov', 'craft': 'ISS'},
            {'name': 'Luca Parmitano', 'craft': 'ISS'},
            {'name': 'Andrew Morgan', 'craft': 'ISS'}
           ],
    'number': 6}
'''