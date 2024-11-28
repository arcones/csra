import argparse
import sys
import re


def get_version_from_setup():
    with open("setup.py", "r") as file:
        content = file.read()
        match = re.search(r"version=['\"]([^'\"]+)['\"]", content)
        if match:
            return match.group(1)
        else:
            raise ValueError("Version not found in setup.py")


def main():
    parser = argparse.ArgumentParser(description="Collect NIH NCBI SRA metadata of several GEO studies in one search")

    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s version {get_version_from_setup()}")
    parser.add_argument("-q", "--query", nargs="+", type=str, help="The NIH NCBI query between quotes", required=True)
    args = parser.parse_args()

    if args.query:
        if len(args.query) > 1:
            print("Error: It looks like your query isn't quoted.")
            print("Usage: csra \"your query here\"")
            sys.exit(1)
        else:
            query = " ".join(args.query)
            print(f"Received query: {query}")


if __name__ == "__main__":
    main()
