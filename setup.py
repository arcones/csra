from setuptools import setup

setup(
    name="csra",
    version="0.1.0",
    packages=["sra_collector"],
    entry_points={
        "console_scripts": [
            "csra=sra_collector.cli:main",
        ]
    },
)
