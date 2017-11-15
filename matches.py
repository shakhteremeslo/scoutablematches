import requests, json, sys

key = sys.argv[1]
headers = {"X-TBA-Auth-Key":key}
#url = "https://www.thebluealliance.com/api/v3/team/frc" + input("Which team do you want to choose? ")

#content = json.loads(requests.get(url, headers=headers).text)

team_events = {"frc1257":"2017mrcmp"}

def isPlayoffs(teamKey, eventKey):
    matches = json.loads(requests.get("http://www.thebluealliance.com/api/v3/team/" + teamKey + "/event/" + eventKey + "/matches/keys", headers=headers).text)
    playoffs = False
    for match in matches:
        if match[len(eventKey)+1:len(eventKey)+3] != "qm":
            playoffs = True
    return playoffs

print(isPlayoffs("frc1257","2017mrcmp"))
#def isVideo(
#
#for key in team_events:
#    if isPlayoffs(key, team_events[key]):
