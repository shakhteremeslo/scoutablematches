# scoutablematches
import requests, json

key = 
headers = {"X-TBA-Auth-Key":key}
url = "https://www.thebluealliance.com/api/v3/team/frc" + input("Which team do you want to choose? ")

def isPlayoffs(teamKey, eventKey):
    

content = json.loads(requests.get(url, headers=headers).text)
