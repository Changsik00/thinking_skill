from abc import ABC, abstractmethod
from typing import List, Set


class SyncRepository(ABC):
    @abstractmethod
    def list_all_chroma_ids(self) -> Set[str]:
        """List all Document IDs stored in ChromaDB."""
        pass

    @abstractmethod
    def delete_chroma_documents(self, ids: List[str]) -> int:
        """
        Delete documents from ChromaDB by IDs.
        Returns the number of deleted documents.
        """
        pass

    @abstractmethod
    def list_all_file_ids(self) -> Set[str]:
        """
        Scan the filesystem and return a set of expected Document IDs derived from filenames.
        Note: The ID generation logic must match what was used during save.
        """
        pass
