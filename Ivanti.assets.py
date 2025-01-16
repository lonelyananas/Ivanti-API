import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

key = os.environ['stg_heat_api_key']
stg_url = os.environ['stg_url']

url = stg_url + "CIs"

params = {
    "Filter": "ivnt_AssetFullType eq 'Computer'",
    "top": "10"
}

headers = {
	"Authorization": key
}
response = requests.get(url, headers=headers, params=params)
#assets = json.dumps(response.json(), indent=4)


print(response.json())


# Test Comment to test Git and GitHub functionality.