# app/infrastructure/automation/n8n_adapter.py
import os
import requests
from dotenv import load_dotenv
from app.domain.entities import DebateResult
from app.domain.interfaces import NerveSystem

class N8nAdapter(NerveSystem):
    """
    Implementation of NerveSystem that triggers n8n webhooks.
    """
    def __init__(self):
        load_dotenv()
        self.webhook_url = os.getenv("N8N_WEBHOOK_URL")

    def trigger(self, result: DebateResult) -> None:
        if not self.webhook_url:
            print("[System]: N8N_WEBHOOK_URL is not set. Skipping automation.")
            return

        payload = {
            "topic": result.topic,
            "summary": result.content,
            "timestamp": result.created_at
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=5)
            if response.status_code == 200:
                print("[System]: n8n Webhook triggered successfully")
            else:
                print(f"[System]: n8n Webhook failed with status {response.status_code}")
        except Exception as e:
            print(f"[System]: Failed to trigger n8n Webhook: {e}")
