import sys
import time

import requests


def verify_sse():
    url = "http://localhost:8000/sse"
    print(f"Checking {url}...")

    for i in range(5):
        try:
            # We use stream=True to avoid hanging forever, but we just want to see if it connects
            with requests.get(url, stream=True, timeout=2) as r:
                print(f"Status Code: {r.status_code}")
                if r.status_code == 200:
                    print("Success: SSE Endpoint is up and responding!")
                    return True
                else:
                    print(f"Failed: Unexpected status code {r.status_code}")
                    return False
        except Exception as e:
            print(f"Attempt {i + 1}: Connection failed ({e})")
            time.sleep(1)

    print("Error: Could not connect to SSE endpoint after multiple attempts.")
    return False


if __name__ == "__main__":
    if not verify_sse():
        sys.exit(1)
