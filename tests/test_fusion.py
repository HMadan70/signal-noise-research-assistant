from research_agent.fusion import fuse_rankings


def test_agreeing_lists_keep_their_order():
    fused = fuse_rankings({"keyword": ["a", "b"], "semantic": ["a", "b"]})
    assert [result["id"] for result in fused] == ["a", "b"]
