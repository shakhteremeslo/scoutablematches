import requests, json, sys

key = sys.argv[1]
headers = {"X-TBA-Auth-Key":key}

team_events = {"frc1257":"2017mrcmp"}

def isVideo(matchKey):
    content = json.loads(requests.get("http://www.thebluealliance.com/api/v3/match/" + matchKey, headers=headers).text)
    if content["videos"] == []:
        return False
    else:
        return True

def isPlayoffs(teamKey, eventKey):
    matchLookup = json.loads(requests.get("http://www.thebluealliance.com/api/v3/team/" + teamKey + "/event/" + eventKey + "/matches/keys", headers=headers).text)
    matches = []
    for key in matchLookup:
        if isVideo(key):
            matches.append(key)
    types = []
    max_type = ""
    for match in matches:
        type = ""
        for i in match.split("_")[1]:
            if i.isdigit():
                break
            else:
                type += i
        types.append(type)
    for m in types:
        if m == "f":
            max_type = "f"
            break
        elif m == "sf":
            max_type = "sf"
            break
        elif m == "qf":
            max_type = "qf"
            break
        else:
            max_type = "qm"
    return matches, max_type

print(isPlayoffs("frc3130","2017mndu2"))