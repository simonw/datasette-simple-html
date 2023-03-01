from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "fn,input,expected",
    (
        ("html_strip_tags", "<p>foo</p>", "foo"),
        ("html_escape", "<p>foo</p>", "&lt;p&gt;foo&lt;/p&gt;"),
        ("html_unescape", "&lt;p&gt;You&#x27;ll&lt;/p&gt;", "<p>You'll</p>"),
    ),
)
async def test_simple_html(fn, input, expected):
    ds = Datasette(memory=True)
    await ds.invoke_startup()
    response = await ds.client.get(
        "/_memory.json",
        params={"_shape": "array", "sql": f"select {fn}(:input) as x", "input": input},
    )
    result = response.json()[0]["x"]
    assert result == expected
