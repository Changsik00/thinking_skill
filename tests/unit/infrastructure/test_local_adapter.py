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

def test_save_with_long_filename_and_special_chars(tmp_path, monkeypatch):
    """Test saving a file with very long topic and special characters."""
    vault_path = tmp_path / "vault"
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(vault_path))
    adapter = LocalAdapter()
    
    # Topic with > 255 chars and special chars (newlines, slashes)
    long_topic = "A" * 300 + "\n/\\:*?\"<>|" + "End"
    
    result = DebateResult(
        topic=long_topic,
        content="Content",
        model="test",
        created_at="now"
    )
    
    # Should not raise OSError
    file_path = adapter.save(result)
    
    assert os.path.exists(file_path)
    filename = os.path.basename(file_path)
    assert len(filename) < 255  # Standard filesystem limit
    assert "\n" not in filename
    assert "/" not in filename

def test_list_debates(tmp_path, monkeypatch):
    """Test resolving list of debates from markdown files."""
    vault_path = tmp_path / "vault"
    vault_path.mkdir()
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(vault_path))
    adapter = LocalAdapter()

    # Create dummy files
    # File 1: Recent
    (vault_path / "2024-01-02_Topic_B.md").write_text(
        "---\ntopic: Topic B\nmodel: gpt-4\ndate: 2024-01-02\n---\n\nContent B"
    )
    # File 2: Older
    (vault_path / "2024-01-01_Topic_A.md").write_text(
        "---\ntopic: Topic A\nmodel: gpt-3\ndate: 2024-01-01\n---\n\nContent A"
    )
    # File 3: Not text (should be ignored)
    (vault_path / "image.png").write_text("binary")

    results = adapter.list_debates(limit=5)
    
    assert len(results) == 2
    # Check order (Recent first because of filename sort desc)
    assert results[0].topic == "Topic B"
    assert results[1].topic == "Topic A"

def test_get_debate(tmp_path, monkeypatch):
    """Test retrieving a specific debate by topic."""
    vault_path = tmp_path / "vault"
    vault_path.mkdir()
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(vault_path))
    adapter = LocalAdapter()

    # Create target file
    filename = "2024-01-01_Target_Topic.md"
    (vault_path / filename).write_text(
        "---\ntopic: Target Topic\nmodel: gpt-4\ndate: 2024-01-01\n---\n\nFound Me"
    )

    # 1. Exact Name Search (simulated by sanitize matching)
    result = adapter.get_debate("Target Topic")
    assert result is not None
    assert result.content == "Found Me"
    assert result.topic == "Target Topic"

    # 2. Not Found
    result_none = adapter.get_debate("Non Existent")
    assert result_none is None
