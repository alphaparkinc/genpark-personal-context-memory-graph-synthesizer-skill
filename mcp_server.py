import json, sys
from client import PersonalContextMemoryGraphSynthesizerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "personal-context-memory-graph-synthesizer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "synthesize_context_graph", "description": "Synthesizes multi-source personal episodic memories into decay-weighted briefings before meetings or negotiations."}]}}
    elif method == "tools/call":
        client = PersonalContextMemoryGraphSynthesizerClient()
        res = client.synthesize_context_graph()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = PersonalContextMemoryGraphSynthesizerClient()
        print(json.dumps(client.synthesize_context_graph(), indent=2))
