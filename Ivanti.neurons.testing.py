import requests
import json
import re
from dotenv import load_dotenv
import os


# Load environment variables an assign values to global variables

load_dotenv()

client_id = os.environ["X-ClientId"]
tenant_id = os.environ["X-TenantId"]
client_secret = os.environ["X-ClientSecret"]
key = os.environ["X-RapidAPI-Key"]
host = os.environ["X-RapidAPI-Host"]
user = os.environ["USER"]
rapid_url = os.environ["rapid_url"]


url = rapid_url + "Token"

headers = {
	"X-ClientId": client_id,
    "X-TenantId": tenant_id,
    "X-ClientSecret": client_secret,
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers)

print(response.__dict__)