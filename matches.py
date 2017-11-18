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

#determines which matches have video, the types of those matches, and the max match type reached at the event
def matchLister(teamKey, eventKey):
    matchLookup = json.loads(requests.get("http://www.thebluealliance.com/api/v3/team/" + teamKey + "/event/" + eventKey + "/matches/keys", headers=headers).text)
    #matches is the set of matches a team played at an event which have video
    matches = []
    for key in matchLookup:
        if isVideo(key):
            matches.append(key)
    #matchdict holds the sorted lists of matches with video by type
    matchdict = {}
    #max_type holds the highest type of match reached in the event
    max_type = ""
    #loop adds match keys to the proper values in matchdict
    for match in matches:
        type = ""
        for i in match.split("_")[1]: #splits match key by underscore and grabs match type and number
            if i.isdigit():
                break
            else:
                type += i
        if type in matchdict:
            matchdict[type].append(match)
        else:
            matchdict[type] = [match]
    #determines max_type
    if "f" in matchdict:
        max_type = "f"
    elif "sf" in matchdict:
        max_type = "sf"
    elif "qf" in matchdict:
        max_type = "qf"
    else:
        max_type = "qm"
    return matchdict, max_type

#determines which matches to prescout
def toScout(dicttypeset):
    #takes input from matchLister as list
    matchdict = dicttypeset[0]
    max_type = dicttypeset[1]
    #scoutlist holds matches to prescout
    scoutlist = []
    #playoffs is obvious
    playoffs = False
    if max_type == "":
        playoffs = None
        scoutlist = "No matches found."
    elif max_type != "qm":
        playoffs = True
    #loop picks max playoff match then tries to pick quals, finals, semis, and quarters in that order
    if playoffs:
        scoutlist.append(matchdict[max_type].pop(-1))
        try:
            try:
                try:
                    try:
                        scoutlist.append(matchdict["qm"][-1])
                    except:
                        scoutlist.append(matchdict["f"][-1])
                except:
                    scoutlist.append(matchdict["sf"][-1])
            except:
                scoutlist.append(matchdict["qf"][-1])
        except:
            scoutlist.append("No more matches found.")
    #loop picks quals
    elif not playoffs:
        scoutlist.append(matchdict["qm"].pop(-1))
        try:
            scoutlist.append(matchdict["qm"][-1])
        except:
            scoutlist.append("No more matches found.")
    return scoutlist

print(toScout(matchLister("frc1257","2017pahat")))
# print(toScout(matchLister("frc1257","2017mrcmp")))