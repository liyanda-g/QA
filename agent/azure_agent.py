import requests
from requests.auth import HTTPBasicAuth

ORG = "YOUR_ORG"
PROJECT = "YOUR_PROJECT"
PAT = "YOUR_PAT"

def fetch_work_item(work_item_id):
    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=7.0"

    response = requests.get(url, auth=HTTPBasicAuth('', PAT))

    print("Status Code:", response.status_code)
    print("Response Text:\n", response.text)

    if response.status_code != 200:
        raise Exception("Failed to fetch work item")

    return response.json()
