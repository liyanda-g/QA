response = requests.get(
    url,
    auth=HTTPBasicAuth('', PAT)
)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

data = response.json()
