import argparse
import ast
from pathlib import Path


class ImportVisitor(ast.NodeVisitor):
    def visit_Import(self, node):
        for name in node.names:
            print(f"Imported {name.name}")

    def visit_ImportFrom(self, node):
        module = node.module
        for name in node.names:
            print(f"Imported {name.name} from {node.module}")


def visit_path(filepath: str) -> None:
    path = Path(filepath)
    contents = path.read_text()
    tree = ast.parse(contents)
    ImportVisitor().visit(tree)



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()

    visit_path(args.filepath)

if __name__ == "__main__":
    main()
