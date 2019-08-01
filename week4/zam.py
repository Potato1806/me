# curl -X GET 
# --header "Accept: application/json" 
# --header "user-key: 513c31afb6421ca27c84b21975f69ef6" 
# "https://developers.zomato.com/api/v2.1/categories"
import requests
import json

headers = {"Accept": "application/json", 
           "user-key": "513c31afb6421ca27c84b21975f69ef6"}
r = requests.get("https://developers.zomato.com/api/v2.1/categories", headers=headers)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print()
    print(the_json["categories"])
    print()
    print([x["categories"]["name"] for x in the_json["categories"]])