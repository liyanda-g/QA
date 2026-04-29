import requests
from requests.auth import HTTPBasicAuth

ORG = "your-org"
PROJECT = "your-project"
PAT = "your-pat"

def fetch_work_item(work_item_id):
    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=7.0"
    
    response = requests.get(url, auth=HTTPBasicAuth('', PAT))
    data = response.json()

    return {
        "title": data['fields'].get('System.Title'),
        "description": data['fields'].get('System.Description')
    }

def generate_test_cases(title, description):
    return f"""
# Test Cases for {title}

## TC1
Verify valid lease creation

## TC2
Validate mandatory fields

## TC3
Validate tenant requirement

## TC4
Validate date logic
"""

if __name__ == "__main__":
    work_item = fetch_work_item("21575")

    test_cases = generate_test_cases(
        work_item["title"],
        work_item["description"]
    )

    with open("generated-test-cases.md", "w") as f:
        f.write(test_cases)

    print("Test cases generated!")
