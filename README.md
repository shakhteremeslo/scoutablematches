# scoutablematches
import requests, json

key = 
headers = {"X-TBA-Auth-Key":key}
url = "https://www.thebluealliance.com/api/v3/team/frc" + input("Which team do you want to choose? ")

content = json.loads(requests.get(url, headers=headers).text)

team_events = {"frc1257":"mrcmp2017"}

def isPlayoffs(teamKey, eventKey):
    matches = json.loads(requests.get("http://www.thebluealliance.com/api/v3/team/" + teamKey + "/event/" + eventKey + "/matches", headers=headers).text)
    for match in matches:
        if match[len(eventKey)+1:len(eventKey)+3] != "qm":
            return True
        else:
            pass

def isVideo(

for key in team_events:
    if isPlayoffs(key, team_events[key]):
        
