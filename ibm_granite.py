import requests
import os

def call_ibm_granite(prompt: str) -> dict:
    API_KEY = os.getenv("IBM_API_KEY")
    PROJECT_ID = os.getenv("IBM_PROJECT_ID")
    URL = "https://us-south.ml.cloud.ibm.com"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token(API_KEY)}"
    }

    payload = {
    "model_id": "ibm/granite-3-3-8b-instruct", 
    "input": prompt,
    "project_id": PROJECT_ID,
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 512,
        "temperature": 0.7,
        "stop_sequences": ["\n\n"]
    }
}


    response = requests.post(
    f"{URL}/ml/v1/text/generation?version=2025-03-25",
    json=payload,
    headers=headers
)

    if response.status_code == 200:
        output = response.json()["results"][0]["generated_text"]
        # basic post-processing
        sections = output.split("Action Items:")
        return {
            "summary": sections[0].replace("Summary:", "").strip(),
            "action_items": "Action Items:" + sections[1].strip() if len(sections) > 1 else ""
            "API CALL SUCCESSFUL"
        }
    else:
        return {"summary": "IBM call failed.", "action_items": "Error."}


def get_token(api_key):
    token_url = "https://iam.cloud.ibm.com/identity/token"
    data = {"apikey": api_key, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(token_url, data=data, headers=headers)
    return res.json()["access_token"]
