# utils/storage.py
import os
import re
from datetime import datetime

ARCHIVE_DIR = "data/archives"

def sanitize_filename(name: str) -> str:
    # Remove invalid characters and replace spaces with underscores
    return re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")

def save_to_markdown(topic: str, content: str) -> str:
    """
    Saves the content to a markdown file in data/archives.
    Returns the absolute path of the saved file.
    """
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_topic = sanitize_filename(topic)
    filename = f"{timestamp}_{safe_topic}.md"
    file_path = os.path.join(ARCHIVE_DIR, filename)
    
    markdown_content = f"""# Topic: {topic}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Final Conclusion
{content}
"""
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    return os.path.abspath(file_path)
