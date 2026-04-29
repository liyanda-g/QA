import requests
from requests.auth import HTTPBasicAuth

ORG = "YOUR_ORG"
PROJECT = "MetadataCollection"
PAT = "YOUR_PAT"

def fetch_work_item(work_item_id):
    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=7.0"

    response = requests.get(url, auth=HTTPBasicAuth('', PAT))

    print("Status Code:", response.status_code)
    print("Raw Response:\n", response.text)

    # ❗ Stop here if not successful
    if response.status_code != 200:
        print("❌ Request failed. Fix credentials or URL.")
        return None

    return response.json()
