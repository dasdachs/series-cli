from setuptools import setup


setup(
    name="series-cli",
    version="0.1",
    install_requires=[
        "Click",
        "Requests",
    ],
    entry_points="""
        [console_scripts]
        series=series-cli:main
    """,
)
