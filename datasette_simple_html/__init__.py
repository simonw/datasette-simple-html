from datasette import hookimpl
import html
import re

tag_re = re.compile(r"<[^>]*>")


def strip_tags(text):
    "A very naive tag stripping implementation"
    return tag_re.sub("", text)


@hookimpl
def prepare_connection(conn):
    conn.create_function("html_strip_tags", 1, strip_tags)
    conn.create_function("html_escape", 1, html.escape)
    conn.create_function("html_unescape", 1, html.unescape)
