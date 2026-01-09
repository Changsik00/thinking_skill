import os
import pytest
import datetime
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.domain.entities import DebateResult

@pytest.fixture
def clean_env(monkeypatch):
    """Clean up environment variables for testing."""
    monkeypatch.delenv("OBSIDIAN_VAULT_PATH", raising=False)

def test_config_default_path(clean_env):
    """Test default path when env var is not set."""
    adapter = LocalAdapter()
    assert adapter.archive_dir == "data/archives"

def test_config_from_env(monkeypatch):
    """Test path from environment variable."""
    test_path = "/tmp/test/obsidian"
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", test_path)
    adapter = LocalAdapter()
    assert adapter.archive_dir == test_path

def test_save_with_frontmatter(tmp_path, monkeypatch):
    """Test saving a file includes YAML Frontmatter."""
    # Setup
    vault_path = tmp_path / "vault"
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(vault_path))
    
    adapter = LocalAdapter()
    
    result = DebateResult(
        topic="AI Safety",
        content="Debate Content Here",
        model="gemini-test",
        created_at="2024-01-01 12:00:00"
    )
    
    # Execute
    file_path = adapter.save(result)
    
    # Verify
    assert os.path.exists(file_path)
    assert str(vault_path) in file_path
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check Frontmatter
    assert content.startswith("---\n")
    assert "type: debate" in content
    assert 'topic: "AI Safety"' in content
    assert 'model: "gemini-test"' in content
    assert "tags: [macs, agent, debate]" in content
    assert "---\n\n# Topic: AI Safety" in content
    assert "Debate Content Here" in content
