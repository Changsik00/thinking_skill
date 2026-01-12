# Imports for Combined Server (LLM + MCP)
from fastapi import FastAPI
from mcp.server.fastmcp import Context, FastMCP

from app.domain.entities import DebateResult
from app.infrastructure.automation.n8n_adapter import N8nAdapter
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain
from app.infrastructure.storage.file_persona_repository import FilePersonaRepository
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.interfaces.api.openai_router import (
    get_run_debate_use_case,
)
from app.interfaces.api.openai_router import (
    router as openai_router,
)
from app.usecases.manage_debates import GetDebateUseCase, ListDebatesUseCase
from app.usecases.run_debate import RunDebateUseCase
from app.usecases.sync_debates import SyncDebatesUseCase

# Initialize Server
mcp = FastMCP("thingking", host="0.0.0.0")

# Dependency Injection
# Note: In a production app, we might use a DI container.
# Here we instantiate directly as per MVP patterns used so far.
adapter = LocalAdapter()
list_use_case = ListDebatesUseCase(adapter)
get_use_case = GetDebateUseCase(adapter)


@mcp.resource("debate://list")
async def list_debates() -> str:
    """List recent debates"""
    debates = await list_use_case.execute(limit=20)

    lines = ["# Recent Debates"]
    for d in debates:
        # Simple markdown list
        lines.append(f"- {d.topic} (Date: {d.created_at}, Model: {d.model})")

    return "\n".join(lines)


@mcp.resource("debate://{topic}")
async def get_debate(topic: str) -> str:
    """Get full debate content by topic"""
    result = await get_use_case.execute(topic)
    if not result:
        return f"Debate with topic '{topic}' not found."

    return f"""# {result.topic}
Date: {result.created_at}
Model: {result.model}

{result.content}
"""


@mcp.tool()
async def search_debates(query: str, ctx: Context) -> str:
    """Search debates by keyword (searches topic and content)"""
    # Currently implemented as in-memory filter over recent debates.
    # Future improvement: Connect to ChromaDB for semantic search.
    all_debates = await list_use_case.execute(limit=50)
    matches = []

    query_lower = query.lower()
    for d in all_debates:
        if query_lower in d.topic.lower() or query_lower in d.content.lower():
            matches.append(d)

    if not matches:
        return f"No matches found for '{query}'."

    lines = [f"# Search Results for '{query}'"]
    for d in matches:
        lines.append(f"- {d.topic}")

    return "\n".join(lines)


@mcp.tool()
async def save_debate(topic: str, content: str) -> str:
    """Save a debate or conversation with a specific topic and content.
    Useful when you want to persist the current discussion or an analysis result.
    """
    try:
        result = DebateResult(topic=topic, content=content)
        path = adapter.save(result)
        return f"Successfully saved to {path}"
    except Exception as e:
        return f"Failed to save debate. Error: {str(e)}"


# DI for Sync
# import moved to top

sync_use_case = SyncDebatesUseCase(adapter)


@mcp.tool()
async def sync_debates(dry_run: bool = False) -> str:
    """
    Synchronize Obsidian files with ChromaDB.
    Deletes 'orphaned' embeddings from ChromaDB that no longer have a corresponding Markdown file.

    Args:
        dry_run: If True, simulates the sync and reports what would be deleted.
    """
    try:
        result = sync_use_case.execute(dry_run=dry_run)

        mode_str = "[DRY RUN] " if result.get("dry_run") else ""
        examined = result.get("examined_count", 0)
        found = result.get("found_garbage_count", 0)
        deleted = result.get("deleted_count", 0)

        return (
            f"{mode_str}Sync Report:\n"
            f"- Total Chroma Documents Examined: {examined}\n"
            f"- Orphaned Documents Found: {found}\n"
            f"- Documents Deleted: {deleted}\n"
            f"\nStatus: {'Clean' if found == 0 else 'Cleanup Complete' if not dry_run else 'Cleanup Required'}"
        )
    except Exception as e:
        return f"Sync failed. Error: {str(e)}"


def create_combined_app() -> FastAPI:
    """
    Creates a combined FastAPI app that serves both:
    1. MCP Server (SSE) at /sse
    2. OpenAI Compatible API at /openai/v1
    """
    app = FastAPI(title="Thingking Unified Server")

    # 1. Mount MCP SSE App
    # FastMCP's sse_app is a Starlette/FastAPI compatible app
    app.mount("/sse", mcp.sse_app)

    # app.mount("/sse", mcp.sse_app)

    # 2. Setup Dependencies for OpenAI Router
    # We need to initialize the full stack (Brain + Nerve + Vault)
    nerve = N8nAdapter()
    vault = LocalAdapter()
    persona_repo = FilePersonaRepository()  # Load personas from YAML
    # Inject vault and nerve into brain to enable tools
    brain = LangGraphBrain(memory=vault, nerve=nerve, persona_repo=persona_repo)

    run_debate_use_case = RunDebateUseCase(brain=brain, memory=vault, nerve=nerve)

    # Override dependency
    app.dependency_overrides[get_run_debate_use_case] = lambda: run_debate_use_case

    # 3. Include OpenAI Router
    app.include_router(openai_router)

    return app


# Expose 'app' for Uvicorn
app = create_combined_app()

if __name__ == "__main__":
    import sys

    if "--sse" in sys.argv:
        import uvicorn

        print("Starting Unified Server (MCP + OpenAI) on http://0.0.0.0:8000")
        print("- MCP SSE: http://0.0.0.0:8000/sse")
        print("- OpenAI API: http://0.0.0.0:8000/openai/v1")

        # Run the combined app
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        mcp.run()
