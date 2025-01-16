import requests
import json
import re
from dotenv import load_dotenv
import os


# Load environment variables an assign values to global variables

load_dotenv()

prod_url = os.environ["prod_url"]
key = os.environ["Heat_API_Key"]


def get_active_req_ids():

    url = prod_url + 'ServiceReqs'
    
    params = {
        '$filter' : "Status eq 'Active' and OwnerTeam eq 'CDI InfoSec - Firewall & VPN'",
    }
    headers = {
    	'Authorization': key
    }
    
    response = requests.get(url, headers=headers, params=params)
    activereqs = response.json()
    
    Req_pages = int((activereqs["@odata.count"]//25))
    
    if Req_pages > 0:
        skip = 25
        i=1
        for i in range(1, Req_pages + 1):
            i+=1
            loop_params = {
                '$filter' : "Status eq 'Active' and OwnerTeam eq 'CDI InfoSec - Firewall & VPN'",
                '$skip' : skip,
            }
            
            response = requests.get(url, headers=headers, params=loop_params)
            activereqs += response.json()
            skip += 25
    
        
    activereqids = [x['RecId']for x in activereqs["value"] if 'RecId' in x]

    
    return activereqids, activereqs

    
def get_params_of_active_reqs(reqs):

    url = prod_url + 'ServiceReqParams'
    
    headers = {
    	'Authorization': key
    }

    paramassets = []

    for reqid in reqs:
        
        params = {
            #'$filter' : "ParameterName eq 'Request_Type' and ParameterValue eq 'Firewall Policy Change'",
            '$filter' :  "ParentLink_RecId eq '{}'".format(reqid)
        }

        response = requests.get(url, headers=headers, params=params)

        paramassets += response.json()["value"]
    

    active_id_list = [x for x in paramassets if (x["ParameterName"] == 'Request_Type') and (x["ParameterValue"] == 'Firewall Policy Change')]
        
    #print(len(active_id_list))
    
    return active_id_list

def combine_params_and_active_reqs(reqs, params):
    combined_dict=[]
    for y in params:
        for x in reqs:
            if "ParentLink_RecID" in y:
                if y["ParentLink_RecID"] == x["RecId"]:
                    for z in y.copy():
                        y["Parameter_{}".format(z)] =  y.pop(z)
                    #for t in x:
                    #    if z == t:
                    combined_dict.append(y | x)
            
        else:
            continue
     
    return combined_dict

def main():
    
    activeids = get_active_req_ids()

    paramsids = get_params_of_active_reqs(activeids[0])

    z = combine_params_and_active_reqs(activeids[1]["value"], paramsids)
    
    test_null_removal = [ele for ele in ({key: val for key, val in sub.items() if val}
                       for sub in z) if ele]
    
    #print(json.dumps(z, indent=4))
    print(len(z))
    print(test_null_removal)

if __name__=="__main__":
    main()
