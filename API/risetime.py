import requests
import json
from datetime import datetime
import apiparameters 

dic_data=apiparameters.data
print(dic_data)

risetime=[]
for i in range(len(dic_data["response"])):
    rtime=dic_data["response"][i]["risetime"]
    risetime.append(rtime)
print(risetime)

times=[]

for rt in risetime:
    time=datetime.fromtimestamp(rt)
    times.append(time)
print(times)

'''
or use this also but below is not the optimised
rstime=[]
for d in dic_data["response"]:
    rstime.append(d["risetime"])
print(rstime)
    
date=
'''


'''
{
    "message": "success",
    "request": {
        "altitude": 100,
        "datetime": 1608145600,
        "latitude": 40.71,
        "longitude": -74.0,
        "passes": 5
    },
    "response": [
        {
            "duration": 586,
            "risetime": 1608150403
        },
        {
            "duration": 593,
            "risetime": 1608204783
        },
        {
            "duration": 649,
            "risetime": 1608210549
        },
        {
            "duration": 581,
            "risetime": 1608216427
        },
        {
            "duration": 569,
            "risetime": 1608222305
        }
    ]
}
'''