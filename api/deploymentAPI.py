# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_P2lL21YAGhayzKcTYjVR4nIFXxbm4D4CCUcw"  # Your Prefect Cloud API key
ACCOUNT_ID = "7701876b-0728-4e3a-9605-540d3abaa2c3"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "f73f7bf2-0937-4f19-bd27-47e7e3547a98"  # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "7cd51cf0-2080-48cf-8879-29746aef4310"  # Your Deployment ID

# Correct API URL to get deployment details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/deployments/{DEPLOYMENT_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    deployment_info = response.json()
    print(deployment_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
