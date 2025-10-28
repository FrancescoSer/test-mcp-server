from mcp.server.fastmcp import FastMCP
#instanzia il server
mcp = FastMCP("TestServer")

#aggiungi tool 1
@mcp.tool()
def test_tool(name: str) -> str:
    return f"Hello, {name}!"

#aggiungi tool 2 puo essere funzione custom qualsiasi
@mcp.tool() #decoratore decorator che permette di aggiungere un tool al server MCP
def add(a: int, b: int) -> int:
    #somma
    return a + b

#aggiungi risorsa 1
@mcp.resource("greeting//{name}")
def get_greeting(name: str) -> str:
    """Ricevi un saluto personalizzato"""
    return f"Hello, {name}!"

#blocco main mcp.run fa girare il server
if __name__ == "__main__":
    mcp.run()


### npx @modelcontextprotocol/inspector --cli
### mcp run test_server.py per avviare il server
### --method tool/list per vedere i tool disponibili
### --method tool/call --tool-name add --tool-arg a=1 tool/arg b=2
### mcp dev test_server.py per avviare il server in modalita development



