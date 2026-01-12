from unittest.mock import patch

import pytest

from app.domain.entities import DebateResult


def test_mcp_server_initialization():
    """Verify MCP server instance and basic setup."""
    from app.interfaces.mcp_server import mcp

    assert mcp.name == "thingking"


@pytest.mark.asyncio
async def test_save_debate_tool():
    """Verify save_debate tool calls adapter.save correctly."""
    # Mock the adapter in the mcp_server module
    with patch("app.interfaces.mcp_server.adapter") as mock_adapter:
        # Setup mock return
        mock_adapter.save.return_value = "/path/to/saved/file.md"

        # Import the function to test
        from app.interfaces.mcp_server import save_debate

        # Execute tool
        topic = "Test Topic"
        content = "Test Content"
        result = await save_debate(topic=topic, content=content)

        # Assertions
        assert "Successfully saved to /path/to/saved/file.md" in result
        mock_adapter.save.assert_called_once()

        # Verify arguments passed to save
        args, _ = mock_adapter.save.call_args
        saved_entity = args[0]
        assert isinstance(saved_entity, DebateResult)
        assert saved_entity.topic == topic
        assert saved_entity.content == content


@pytest.mark.asyncio
async def test_save_debate_tool_failure():
    """Verify save_debate returns error message on exception."""
    with patch("app.interfaces.mcp_server.adapter") as mock_adapter:
        # Simulate an error (e.g., Disk Full)
        mock_adapter.save.side_effect = OSError("Disk Full")

        from app.interfaces.mcp_server import save_debate

        result = await save_debate(topic="Fail", content="Content")

        assert "Failed to save debate" in result
        assert "Disk Full" in result
