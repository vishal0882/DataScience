import requests
from google.adk.agents import Agent

def call_mcp(session_id: str) -> dict:
    """Example function to call your MCP endpoint."""
    url = f"https://fi-mcp-dev-446597266106.europe-west1.run.app/mockWebPage?sessionId={session_id}"
    #url = f"https://fi-mcp-dev-446597266106.europe-west1.run.app/mockWebPage?sessionId={'a555e28f-1473-43c8-80e6-581ea48f482e'}"
   
    #response = requests.get(url)
    response = requests.get(url)
    if response.status_code == 200:
        return {"status": "success", "data": response.text}
    else:
        return {"status": "error", "message": f"HTTP {response.status_code}"}

# Register the agent
root_agent = Agent(
    name="mcp_agent",
    model="gemini-2.0-flash",  # Or another Gemini model
    description="Agent to interact with fi-mcp server via HTTP.",
    instruction="Respond to queries by reaching out to the MCP server using the provided session ID, phone number and OTP.",
    tools=[call_mcp]
)
