import requests
import json

class Tools:
    def __init__(self):
        # Docker 내부 네트워크 주소 사용
        self.base_url = "http://mcpo:8000/thingking"

    def save_debate(self, topic: str, content: str) -> str:
        """
        Save a debate or conversation with a specific topic and content.
        Useful when you want to persist the current discussion or an analysis result.
        
        :param topic: The topic of the debate.
        :param content: The content of the debate.
        """
        url = f"{self.base_url}/save_debate"
        payload = {"topic": topic, "content": content}
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            # mcpo는 결과 JSON 안에 "result" 필드를 포함할 수 있음
            data = response.json()
            return data.get("result", response.text)
        except Exception as e:
            return f"Error saving debate: {str(e)}"

    def search_debates(self, query: str) -> str:
        """
        Search debates by keyword (searches topic and content).
        
        :param query: The search query keyword.
        """
        url = f"{self.base_url}/search_debates"
        payload = {"query": query}
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("result", response.text)
        except Exception as e:
            return f"Error searching debates: {str(e)}"
