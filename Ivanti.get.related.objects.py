import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

prod_url = os.environ["prod_url"]
key = os.environ["Heat_API_Key"]

url = prod_url + "ServiceReqs('41FE26659780464EA6ECA0AE881765FA')/ServiceReqContainsJournal"

headers = {
	'Authorization': key
}

response = requests.get(url, headers=headers,) #params=params)
assets = json.dumps(response.json(), indent=4)

print(response)
print(response.json())