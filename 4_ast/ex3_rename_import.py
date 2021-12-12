import argparse
import ast
from pathlib import Path


class ImportVisitor(ast.NodeVisitor):
    def __init__(self, *, to_rename: str):
        self.to_rename = to_rename
        self.locations = []

    def visit_Import(self, node):
        for name in node.names:
            if name.name == self.to_rename:
                # Line numbers in the AST start at 1, but we'd like
                # them to start at 0, like most things in Python
                self.locations.append(node.lineno - 1)

    def visit_ImportFrom(self, node):
        if node.module == self.to_rename:
            self.locations.append(node.lineno - 1)


def visit_file(file: Path, *, before: str, after: str) -> None:
    visitor = ImportVisitor(to_rename=before)
    contents = file.read_text()
    visitor.visit(ast.parse(contents))
    if not visitor.locations:
        return

    content_list = contents.splitlines()
    for line_no in visitor.locations:
        original_line = content_list[line_no]
        content_list[line_no] = original_line.replace(before, after)

    new_contents = "\n".join(content_list)
    file.write_text(new_contents)
    print(f"Rewrote {len(visitor.locations)} occurrence(s) in {file}")


def visit_path(file_or_dir: str, *, before: str, after: str) -> None:
    path = Path(file_or_dir)
    if path.is_dir():
        for p in path.glob("**/*.py"):
            visit_file(p, before=before, after=after)
    else:
        visit_file(path, before=before, after=after)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file_or_dir')
    parser.add_argument('--before')
    parser.add_argument('--after')
    args = parser.parse_args()

    visit_path(args.file_or_dir, before=args.before, after=args.after)

if __name__ == "__main__":
    main()
