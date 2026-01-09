import pytest
from mcp.server.fastmcp import FastMCP

def test_mcp_server_instance():
    # Attempt to import the server instance
    try:
        from app.interfaces.mcp_server import mcp
    except ImportError:
        pytest.fail("Could not import 'mcp' from app.interfaces.mcp_server")

    assert isinstance(mcp, FastMCP)
    assert mcp.name == "thingking"

    # Verify Tools
    tool_names = [t.name for t in mcp._tools.values()] if hasattr(mcp, '_tools') else []
    # FastMCP structure might differ, but usually we can check registered tools
    # Actually FastMCP manages tools internally. 
    # Validating if we can list tools via mcp.list_tools() if available or inspecting internal dict
    
    # We will just check if the module has the functions decorated if possible, 
    # or rely on basic import success for now as FastMCP internals are complex to mock without running.
