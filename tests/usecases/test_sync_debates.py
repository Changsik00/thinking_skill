import pytest
from unittest.mock import MagicMock
from app.usecases.sync_debates import SyncDebatesUseCase
from app.domain.interfaces.sync_repository import SyncRepository

class MockSyncRepository(SyncRepository):
    def __init__(self, chroma_ids, file_ids):
        self.chroma_ids = set(chroma_ids)
        self.file_ids = set(file_ids)
        self.deleted_ids = []

    def list_all_chroma_ids(self):
        return self.chroma_ids

    def list_all_file_ids(self):
        return self.file_ids

    def delete_chroma_documents(self, ids):
        self.deleted_ids.extend(ids)
        # Remove from internal store to simulate deletion
        for i in ids:
            if i in self.chroma_ids:
                self.chroma_ids.remove(i)
        return len(ids)

def test_sync_no_garbage():
    # DB and File have same IDs
    repo = MockSyncRepository(["A", "B"], ["A", "B"])
    use_case = SyncDebatesUseCase(repo)
    
    result = use_case.execute()
    
    assert result["found_garbage_count"] == 0
    assert result["deleted_count"] == 0
    assert len(repo.deleted_ids) == 0

def test_sync_with_garbage():
    # DB has "C" which is not in File
    repo = MockSyncRepository(["A", "B", "C"], ["A", "B"])
    use_case = SyncDebatesUseCase(repo)
    
    result = use_case.execute()
    
    assert result["found_garbage_count"] == 1
    assert result["deleted_count"] == 1
    assert "C" in repo.deleted_ids
    assert "C" not in repo.chroma_ids

def test_sync_dry_run():
    # DB has "C" but dry_run is True
    repo = MockSyncRepository(["A", "B", "C"], ["A", "B"])
    use_case = SyncDebatesUseCase(repo)
    
    result = use_case.execute(dry_run=True)
    
    assert result["found_garbage_count"] == 1
    assert result["deleted_count"] == 0 # Should not delete
    assert len(repo.deleted_ids) == 0
    assert "C" in repo.chroma_ids # Should still exist
