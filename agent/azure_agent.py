import requests
from requests.auth import HTTPBasicAuth

ORG = "MetadataCollection"   # example: liyanda-g or your org name
PROJECT = "QA"
PAT = "yl6smwtd3y7mcmgitf33bspeagkn5kdtramujhfoi2g52ocu3n2a"

def fetch_work_item(work_item_id):
 url = f"http://galaxy80-vm1:8080/tfs/MetadataCollection/QA/_apis/wit/workitems/{work_item_id}?api-version=6.0"
    response = requests.get(url, auth=HTTPBasicAuth('', PAT))

    print("\n===== DEBUG OUTPUT =====")
    print("Status Code:", response.status_code)
    print("Response Text:\n", response.text)
    print("========================\n")

    # ❗ DO NOT call .json() yet
    return response


# RUN
fetch_work_item("21575")
