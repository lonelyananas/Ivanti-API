import requests
import json
from dotenv import load_dotenv, dotenv_values
import os



load_dotenv()

key = os.environ["Heat_API_Key"]
prod_url = os.environ["prod_url"]

url = prod_url + "ServiceReqs"

params = {
    #'$filter' : "(ParameterName eq 'Request_Type') and (ParameterValue eq 'Firewall Policy Change')",
    #'$skip' : 600
    #'RecID':"16A293363BDF487A841DF41195E2F660"
    '$filter': "RecID eq 'A05155BA36B84B27A634DB8857D699D4'"
}

headers = {
	'Authorization': key
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
assets = json.dumps(response.json(), indent=4)

print(assets)
print(response.url)
