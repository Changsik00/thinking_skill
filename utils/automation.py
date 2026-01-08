# utils/automation.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def trigger_n8n_workflow(topic: str, summary: str) -> None:
    """
    Triggers an n8n webhook with the debate summary.
    """
    webhook_url = os.getenv("N8N_WEBHOOK_URL")
    if not webhook_url:
        print("\n[System]: N8N_WEBHOOK_URL is not set. Skipping automation.")
        return

    payload = {
        "topic": topic,
        "summary": summary,
        "source": "MACS_Agent"
    }
    
    try:
        response = requests.post(webhook_url, json=payload, timeout=5)
        if response.status_code == 200:
            print(f"\n[System]: n8n Webhook triggered successfully.")
        else:
            print(f"\n[System]: n8n Webhook failed with status {response.status_code}")
    except Exception as e:
        print(f"\n[System]: Failed to trigger n8n: {e}")
