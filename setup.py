from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-simple-html",
    description="Datasette SQL functions for very simple HTML operations",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-simple-html",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-simple-html/issues",
        "CI": "https://github.com/simonw/datasette-simple-html/actions",
        "Changelog": "https://github.com/simonw/datasette-simple-html/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_simple_html"],
    entry_points={"datasette": ["simple_html = datasette_simple_html"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
