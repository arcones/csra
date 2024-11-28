import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Collect NIH NCBI SRA metadata of several GEO studies in one search")

    parser.add_argument("-q", "--query", nargs="+", type=str, help="The NIH NCBI query between quotes", required=True)
    args = parser.parse_args()

    if len(args.query) > 1:
        print("Error: It looks like your query isn't quoted.")
        print("Usage: cli.py \"your query here\"")
        sys.exit(1)

    query = " ".join(args.query)
    print(f"Received query: {query}")


if __name__ == "__main__":
    main()
