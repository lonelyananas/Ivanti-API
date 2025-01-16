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



# Api call requests limit = 172,800/day (A call to any endpoint is a request)
# Rate Limit = 150 requests per minute.

# Function to retrieve Bearer token. Token is valid for

def get_token():
        
    url = "https://people-and-device-inventory.p.rapidapi.com/api/apigatewaydataservices/v1/Token"

    headers = {
        "X-TenantId": tenant_id,
    	"X-ClientId": client_id,
        "X-ClientSecret": client_secret,
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": host
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception("Authentication failed, check header values for issues or expired keys. Response status was, " + str(response.status_code))
    else:
        token=(response.text)
        return token
    

#Determine if scrollID value exists. Conditional for first call and subsequent calls.

def get_assets(asset_db):

    url = "https://people-and-device-inventory.p.rapidapi.com/api/apigatewaydataservices/v1/devices"
    
    token = get_token()
    
    headers = {
	"Authorization": "Bearer {}".format(token),
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": host
    }
    
    payload = {"$select": "Network/TCPIP/BoundAdapter/PhysicalAddress,Network/TCPIP/BoundAdapter/IPAddress,Network/TCPIP/BoundAdapter/NetworkID,Network/TCPIP/BoundAdapter/Description,OS/Version,System/ChassisType,ActiveDirectory/DistinguishedName,LDAPUser/PrimaryOwner/LDAPName,LDAPUser/PrimaryOwner/ShortName,Network/TCPIP/HostName,DisplayName"}
    
    response = requests.get(url, headers=headers, params=payload)
    response = response.json()
    
    asset_db += response["value"]
    
    while "@odata.nextLink" in response:
        
        url = response["@odata.nextLink"]
        response = requests.get(url, headers=headers)
        response = response.json()
        
       
        if "@odata.nextLink" in response:
                
                asset_db += response["value"]
                continue
        
        else:
            print("@odata.nextLink value has been exhausted")
            print(response)    
            with open('/Users/{}/Desktop/asset_db.json'.format(user), 'w') as ad:
                data = asset_db
                json.dump(data, ad, ensure_ascii=False)
                print(len(asset_db))
                break

asset_inventory = []
get_assets(asset_inventory)




""" try:
            response = response.json()
        
        except json.decoder.JSONDecodeError:
            
            print("A JSONerror occured")
            print(response.status_code)
            print(response.json())
            print(response.keys())
            print(response)
            
        except TypeError:
            print("A TypeError occured")
            print(response.status_code)
            print(response.json())
            print(response.keys())
            print(response)
        else:"""