import argparse
import ast
from pathlib import Path

import astpretty


def dump_ast(filepath: str) -> None:
    path = Path(filepath)
    contents = path.read_text()
    tree = ast.parse(contents)

    astpretty.pprint(tree)



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()

    dump_ast(args.filepath)

if __name__ == "__main__":
    main()
