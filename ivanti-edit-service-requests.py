import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ['Heat_API_Key']
prod_url = os.environ["prod_url"]

url = prod_url + "ServiceReqs('A05155BA36B84B27A634DB8857D699D4')/ServiceReqContainsJournal"


headers = {
	'Authorization': key
}

response = requests.get(url=url,headers=headers)

print(json.dumps(response.json(), indent=4))