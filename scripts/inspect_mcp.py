from mcp.server.fastmcp import FastMCP

print("Attributes of FastMCP:")
print([a for a in dir(FastMCP) if not a.startswith("_")])

print("\nHelp on FastMCP.run:")
try:
    help(FastMCP.run)
except Exception as e:
    print(e)
