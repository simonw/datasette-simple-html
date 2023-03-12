from datasette import hookimpl
import html
import re

tag_re = re.compile(r"<[^>]*>")


def strip_tags(text):
    "A very naive tag stripping implementation"
    if text is None:
        return None
    return tag_re.sub("", text)


def escape(text):
    if text is None:
        return None
    return html.escape(text)


def unescape(text):
    if text is None:
        return None
    return html.unescape(text)


@hookimpl
def prepare_connection(conn):
    conn.create_function("html_strip_tags", 1, strip_tags)
    conn.create_function("html_escape", 1, escape)
    conn.create_function("html_unescape", 1, unescape)
