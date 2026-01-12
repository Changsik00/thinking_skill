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

    def __init__(self, webhook_url: str = None):
        load_dotenv()
        self.webhook_url = webhook_url or os.getenv("N8N_WEBHOOK_URL")

    def trigger(self, result: DebateResult, target: str = "default") -> str:
        """
        Triggers n8n webhook with the debate result and target destination.

        Args:
            result: The debate result containing topic and content.
            target: The intended destination (e.g., "slack", "blog", "email").

        Returns:
            str: Status message indicating success or failure.
        """
        if not self.webhook_url:
            msg = "N8N_WEBHOOK_URL is not set. Skipping automation."
            print(f"[System]: {msg}")
            return msg

        payload = {
            "topic": result.topic,
            "summary": result.content,
            "timestamp": result.created_at,
            "target": target,  # n8n can use this to route to different nodes (Switch Node)
            "source": "Thingking Brain",
        }

        try:
            # We use a timeout to avoid blocking the agent too long
            response = requests.post(self.webhook_url, json=payload, timeout=5)
            if response.status_code == 200:
                msg = f"Automation triggered successfully for target: {target}"
                print(f"[System]: {msg}")
                return msg
            else:
                msg = f"Automation failed with status {response.status_code}"
                print(f"[System]: {msg}")
                return msg
        except Exception as e:
            msg = f"Failed to trigger automation: {str(e)}"
            print(f"[System]: {msg}")
            return msg
