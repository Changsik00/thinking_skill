from typing import Dict

from app.domain.interfaces.sync_repository import SyncRepository


class SyncDebatesUseCase:
    def __init__(self, repository: SyncRepository):
        self.repository = repository

    def execute(self, dry_run: bool = False) -> Dict[str, int]:
        """
        Synchronize Obsidian files with ChromaDB.
        Deletes ChromaDB records that do not have corresponding files.

        Args:
            dry_run: If True, only returns what would be deleted without executing.

        Returns:
            Dictionary with keys 'deleted_count' and 'examined_count'
        """
        # 1. Get all IDs from DB (Source of potential garbage)
        db_ids = self.repository.list_all_chroma_ids()

        # 2. Get all IDs from Files (Source of Truth)
        file_ids = self.repository.list_all_file_ids()

        # 3. Calculate Diff: In DB but not in Files
        ids_to_delete = list(db_ids - file_ids)

        result = {
            "examined_count": len(db_ids),
            "found_garbage_count": len(ids_to_delete),
            "deleted_count": 0,
            "dry_run": dry_run,
        }

        if not ids_to_delete:
            return result

        if not dry_run:
            deleted = self.repository.delete_chroma_documents(ids_to_delete)
            result["deleted_count"] = deleted

        return result
