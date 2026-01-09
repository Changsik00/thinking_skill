import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    # Define server parameters
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "-m", "app.interfaces.mcp_server"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize connection
            await session.initialize()

            # 1. List Resources
            print("\n>>> Testing Resource Listing (debate://list)...")
            resources = await session.list_resources()
            print(f"Found {len(resources.resources)} resources.")
            for r in resources.resources:
                print(f"- {r.name} ({r.uri})")

            # 2. Call Tool (Search)
            print("\n>>> Testing Tool Execution (search_debates)...")
            tools = await session.list_tools()
            print(f"Found Tools: {[t.name for t in tools.tools]}")
            
            # Executing search
            result = await session.call_tool("search_debates", arguments={"query": "AI"})
            print(f"Search Result:\n{result.content[0].text[:200]}...") # Print first 200 chars

if __name__ == "__main__":
    asyncio.run(run())
