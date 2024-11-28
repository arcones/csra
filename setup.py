from setuptools import setup

setup(
    name="srac",
    version="0.1.0",
    packages=["sra_collector"],
    entry_points={
        "console_scripts": [
            "sra_collector=sra_collector.cli.py:main",
        ]
    },
)
