# app/infrastructure/storage/local_adapter.py
import os
import re
from typing import Optional, List
from datetime import datetime
import chromadb
from app.domain.entities import DebateResult
from app.domain.interfaces import MemoryVault

class LocalAdapter(MemoryVault):
    """
    Implementation of MemoryVault that saves to local filesystem and ChromaDB.
    """
    def __init__(self, archive_dir: str = "data/archives"):
        # Prioritize Environment Variable -> Constructor Argument
        env_path = os.getenv("OBSIDIAN_VAULT_PATH")
        self.archive_dir = env_path if env_path else archive_dir

    def _sanitize_filename(self, name: str) -> str:
        # Replace newlines and tabs with underscore
        name = re.sub(r'[\n\t]', "_", name)
        # Remove invalid chars for filesystem
        name = re.sub(r'[\\/*?:"<>|]', "", name)
        # Replace spaces with underscore
        name = name.replace(" ", "_")
        # Deduplicate underscores
        name = re.sub(r'_+', "_", name)
        # Truncate to safe length (100 chars)
        return name[:100]

    def _save_to_markdown(self, result: DebateResult) -> str:
        os.makedirs(self.archive_dir, exist_ok=True)
        
        safe_topic = self._sanitize_filename(result.topic)
        filename_ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_ts}_{safe_topic}.md"
        file_path = os.path.join(self.archive_dir, filename)
        
        # YAML Frontmatter for Obsidian
        markdown_content = f"""---
type: debate
topic: "{result.topic}"
model: "{result.model}"
date: {result.created_at}
tags: [macs, agent, debate]
---

# Topic: {result.topic}
Date: {result.created_at}

## Final Conclusion
{result.content}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        return os.path.abspath(file_path)

    def _save_to_chroma(self, result: DebateResult) -> None:
        try:
            host = os.getenv("CHROMA_HOST", "localhost")
            port = int(os.getenv("CHROMA_PORT", 8000))
            client = chromadb.HttpClient(host=host, port=port)
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

    def _parse_markdown_file(self, file_path: str) -> Optional[DebateResult]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Simple frontmatter parser
            parts = content.split("---", 2)
            if len(parts) < 3:
                return None # Invalid format
            
            frontmatter_str = parts[1]
            body = parts[2].strip()
            
            metadata = {}
            for line in frontmatter_str.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip().strip('"')
            
            return DebateResult(
                topic=metadata.get("topic", "Unknown"),
                content=body,
                model=metadata.get("model", "Unknown"),
                created_at=metadata.get("date", "")
            )
        except Exception:
            return None

    def list_debates(self, limit: int = 10) -> List[DebateResult]:
        """
        Returns a list of recent debates by scanning filenames in archive_dir.
        Recent files first.
        """
        if not os.path.exists(self.archive_dir):
            return []
            
        files = [f for f in os.listdir(self.archive_dir) if f.endswith(".md")]
        files.sort(reverse=True) # Filenames start with timestamp, so string sort works for date desc
        
        results = []
        for filename in files[:limit]:
            result = self._parse_markdown_file(os.path.join(self.archive_dir, filename))
            if result:
                results.append(result)
        return results

    def get_debate(self, topic: str) -> Optional[DebateResult]:
        """
        Retrieves a specific debate by topic. 
        Searches for the most recent file containing the sanitized topic string.
        """
        if not os.path.exists(self.archive_dir):
            return None

        # Sanitize input topic to match filename convention
        safe_query = self._sanitize_filename(topic)
        
        files = [f for f in os.listdir(self.archive_dir) if f.endswith(".md")]
        files.sort(reverse=True)
        
        for filename in files:
            if safe_query in filename:
                return self._parse_markdown_file(os.path.join(self.archive_dir, filename))
        
        return None

    def save(self, result: DebateResult) -> str:
        """
        Saves to Markdown and ChromaDB. Returns the path of the markdown file.
        """
        # 1. Save to Markdown
        path = self._save_to_markdown(result)
        
        # 2. Save to ChromaDB
        self._save_to_chroma(result)
        
        return path
