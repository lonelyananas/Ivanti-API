register_module_line('IvantiHeatCreateServiceReqExample', 'start', __line__())
### pack version: 1.0.10


import json
from datetime import datetime, timezone, timedelta

start = datetime.now(timezone.utc)
gap = timedelta(minutes=30)
end = start + gap



"""
Use the IvantiHeatCreateServiceReqExample script to create a change object (JSON) in Ivanti Heat.
The script gets the arguments required to create the change, such as category, subject, and so on.
It creates the JSON object and sets it inside the IvantiHeat.CreatechangeJSON context path.
To create a change in Ivanti, execute the script and call the “ivanti-heat-object-create” command where the
fields argument value equals the script output:
!ivanti-heat-object-create object-type=changes fields=${IvantiHeat.CreatechangeJSON}
To add additional fields to the script, log in to the Ivanti platform and go to:
Settings > Buisness objects > change > Fields, and add the field name to the data dictionary above.
Then add the new field argument to the script. See the Ivanti documentation for more information on creating object:
*tenant-url*/help/admin/Content/Configure/API/Create-a-Business-Object.htm
"""


def main():

    requestorlink = demisto.args().get('requested_by')
    team = demisto.args().get('team')
    owner = demisto.args().get('owner')
    _type = demisto.args().get('type')
    category = demisto.args().get('category')
    risk_level = demisto.args().get('risk_level')
    summary = demisto.args().get('summary')
    description = demisto.args().get('description')
    reason = demisto.args().get('reason')
    outage_details = demisto.args().get('outage_details')
    validation_plan = demisto.args().get('validation_plan')
    expected_outcome = demisto.args().get('expected_outcome')
    backout_plan = demisto.args().get('backout_plan')
    template_name = demisto.args().get('template_name')
    requestorlink_recid = demisto.args().get('requestorlink_recid')




    data = {
        "RequestorLink": requestorlink,
        "OwnerTeam": team,
        "Owner": owner,
        "TypeOfChange":_type,
        "Category": category,
        "RiskLevel": risk_level,
        "ScheduledStartDate":str(start),
        "ScheduledEndDate":str(end),
        "Subject": summary,
        "Description": description,
        "Reason": reason,
        "CDI_OutageDetails": outage_details,
        "CDI_ValidationPlan": validation_plan,
        "CDI_ExpectedOutcome": expected_outcome,
        "CDI_BackoutPlan": backout_plan,
        "CDI_TemplateName": template_name,
        "RequestorLink_RecID": requestorlink_recid,
        "RequestorLink_Category": "Employee",
    }

    jdata = json.dumps(data)

    demisto.setContext('IvantiHeat.CreateChangeJSON', jdata)


if __name__ == "__builtin__" or __name__ == "builtins":
    main()

register_module_line('IvantiHeatCreateServiceReqExample', 'end', __line__())


