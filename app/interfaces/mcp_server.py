from mcp.server.fastmcp import FastMCP, Context
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.usecases.manage_debates import ListDebatesUseCase, GetDebateUseCase
from app.domain.entities import DebateResult

# Initialize Server
mcp = FastMCP("thingking")

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

if __name__ == "__main__":
    import sys
    if "--sse" in sys.argv:
        import uvicorn
        print("Starting MCP Server in SSE mode on http://0.0.0.0:8000/sse")
        uvicorn.run(mcp.sse_app, host="0.0.0.0", port=8000)
    else:
        mcp.run()
