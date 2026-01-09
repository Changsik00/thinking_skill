# app/infrastructure/storage/local_adapter.py
import os
import re
from datetime import datetime
import chromadb
from app.domain.entities import DebateResult
from app.domain.interfaces import MemoryVault

class LocalAdapter(MemoryVault):
    """
    Implementation of MemoryVault that saves to local filesystem and ChromaDB.
    """
    def __init__(self, archive_dir: str = "data/archives"):
        self.archive_dir = archive_dir

    def _sanitize_filename(self, name: str) -> str:
        return re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")

    def _save_to_markdown(self, result: DebateResult) -> str:
        os.makedirs(self.archive_dir, exist_ok=True)
        
        safe_topic = self._sanitize_filename(result.topic)
        # Using the created_at from result but sanitize it for filename if needed, 
        # or just generate new timestamp for filename to avoid collisions?
        # Let's use current time for filename to ensure uniqueness on save.
        filename_ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_ts}_{safe_topic}.md"
        file_path = os.path.join(self.archive_dir, filename)
        
        markdown_content = f"""# Topic: {result.topic}
Date: {result.created_at}

## Final Conclusion
{result.content}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        return os.path.abspath(file_path)

    def _save_to_chroma(self, result: DebateResult) -> None:
        try:
            client = chromadb.HttpClient(host='localhost', port=8000)
            collection = client.get_or_create_collection(name="macs_discussions")
            
            timestamp_id = datetime.now().strftime('%Y%m%d%H%M%S')
            safe_topic = self._sanitize_filename(result.topic)
            doc_id = f"{safe_topic}_{timestamp_id}"
            
            collection.add(
                documents=[result.content],
                metadatas=[{"topic": result.topic, "timestamp": result.created_at}],
                ids=[doc_id]
            )
            print(f"[System]: Saved to ChromaDB (ID: {doc_id})")
        except Exception as e:
            print(f"[System]: Failed to save to ChromaDB: {e}")

    def save(self, result: DebateResult) -> str:
        """
        Saves to Markdown and ChromaDB. Returns the path of the markdown file.
        """
        # 1. Save to Markdown
        path = self._save_to_markdown(result)
        
        # 2. Save to ChromaDB
        self._save_to_chroma(result)
        
        return path
