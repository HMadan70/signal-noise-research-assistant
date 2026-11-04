import json

from research_agent.tool_json import parse_calls

TOOLS = {"search": {"query": "string"}}


def test_whole_reply_is_one_call():
    call = {"id": "c1", "tool": "search", "arguments": {"query": "flood"}}
    assert parse_calls(json.dumps({"calls": [call]}), TOOLS) == {"calls": [call]}
