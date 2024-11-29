from setuptools import setup
import re
import os

MODULE_NAME = "sra_collector"

def get_version():
    version_file =  os.path.join(os.path.dirname(__file__), MODULE_NAME, "__init__.py")
    with open(version_file, "r") as f:
        content = f.read()
        version_match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

setup(name="csra", version=get_version(), packages=[MODULE_NAME], entry_points={"console_scripts": [f"csra={MODULE_NAME}.cli:main", ]}, )
