import argparse
import ast
from collections import Counter
from pathlib import Path


class ImportVisitor(ast.NodeVisitor):
    counter = Counter()

    def visit_Import(self, node):
        for name in node.names:
            self.counter[name.name] += 1

    def visit_ImportFrom(self, node):
        self.counter[node.module] += 1


def visit_file(file: Path, *, visitor: ImportVisitor) -> None:
    contents = file.read_text()
    visitor.visit(ast.parse(contents))


def visit_path(file_or_dir: str, *, visitor: ImportVisitor) -> None:
    path = Path(file_or_dir)
    if path.is_dir():
        for p in path.glob("**/*.py"):
            visit_file(p, visitor=visitor)
    else:
        visit_file(path, visitor=visitor)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file_or_dir')
    args = parser.parse_args()

    visitor = ImportVisitor()
    visit_path(args.file_or_dir, visitor=visitor)
    print(visitor.counter.most_common(10))

if __name__ == "__main__":
    main()
