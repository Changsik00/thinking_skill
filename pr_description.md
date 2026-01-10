# Spec 010: OpenWebUI OpenAPI Bridge Integration

## 🎯 Summary
This PR implements the **MCP-to-OpenAPI Bridge** using `mcpo`, enabling OpenWebUI to connect to the local Thingking MCP server despite native UI limitations in v0.6.43.
It establishes a robust connection by running `mcpo` efficiently alongside other services in Docker Compose.

## 📝 Changes

### Infrastructure
- **`docker-compose.yml`**: Added `mcpo` service (ghcr.io/open-webui/mcpo:main).
    - Exposed on port `3001` (host) / `8000` (container).
    - Configured to bridge to `http://host.docker.internal:8000/mcp/sse`.
- **`config/mcpo.json`**: Created configuration tracking the local `thingking` server.

### Tool Registration (Workaround)
- **`config/openwebui_tool_script.py`**: Added a Python script for manual tool registration in OpenWebUI.
    - **Why?**: The native "Import from URL" feature in OpenWebUI exhibited JSON parsing errors (`true` vs `True`) and flaky validation.
    - **How**: This script uses `requests` to call the `mcpo` internal endpoint (`http://mcpo:8000/thingking`) directly from within the OpenWebUI container.

## ✅ Verification
- **Container Status**: `mcpo` container runs and connects to `thingking` via SSE.
- **OpenAPI Endpoint**: Verified via `curl http://localhost:3001/thingking/openapi.json`.
- **Tool Execution**: `save_debate` tool successfully saved a file to `data/archives/` when called from OpenWebUI chat.

## 📌 Usage
To re-register tools in a fresh OpenWebUI instance:
1. Go to **Workspace > Tools > Create Tool**.
2. Paste the content of `config/openwebui_tool_script.py`.
3. Save and enable the tool in **Model Settings**.
