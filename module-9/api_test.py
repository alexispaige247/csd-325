# Alexis Mitchell
# July 15, 2025

import json
import requests

#API for astronaut names
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, indent=4, sort_keys=True)
    print(text)

jprint(response.json())


# API for D&D wizard class
response = requests.get("https://www.dnd5eapi.co/api/classes/wizard")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, indent=4, sort_keys=True)
    print(text)

jprint(response.json())
