import requests, json, sys

#setting up API requests
key = sys.argv[1]
headers = {"X-TBA-Auth-Key":key}

#scoutable event output
team_events = {"frc1257":"2017mrcmp"}

#determines if a match has videos (is "videos" not an empty set)
def isVideo(matchKey):
    content = json.loads(requests.get("http://www.thebluealliance.com/api/v3/match/" + matchKey, headers=headers).text)
    if content["videos"] == []:
        return False
    else:
        return True

#
def isPlayoffs(teamKey, eventKey):
    matchLookup = json.loads(requests.get("http://www.thebluealliance.com/api/v3/team/" + teamKey + "/event/" + eventKey + "/matches/keys", headers=headers).text)
    #matches is the set of matches a team played at an event which have video
    matches = []
    for key in matchLookup:
        if isVideo(key):
            matches.append(key)
    #types is the set of the types of matches with video
    types = []
    #matchdict holds the sorted lists of matches with video by type
    matchdict = {"qm":[],"qf":[],"sf":[],"f":[]}
    #max_type holds the highest type of match reached in the event
    max_type = ""
    #loop makes types list and adds match keys to the proper values in matchdict
    for match in matches:
        type = ""
        for i in match.split("_")[1]:
            if i.isdigit():
                break
            else:
                type += i
        types.append(type)
        matchdict[type].append(match)
    #loop determines max_type
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
    return matchdict, max_type

print(isPlayoffs("frc3130","2017mndu2"))