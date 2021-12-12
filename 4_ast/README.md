# The Abstract Syntax Tree

## Preface

Run `pip install astpretty` before using this section!

Also, while this section is written about python, the concepts are true of most code formatters in other languages. All languages have some sort of abstract syntax tree.

## Introduction

You may be wondering how a tool like `black` or `pyupgrade` works. It's much more complicated than the simple refactors we've done with `sed`. It also seems to contain some knowledge of the python language, since it knows what's in a comment, etc!

The answer is that these tools know about Python's "Abstract Syntax Tree", or the grammar (syntax) of a given python module, parsable via a tree.

## Viewing a file's AST


```bash
python ex1_print_ast.py ex1_simple_file.py
```

What is being printed out here is what Python sees when it looks at the given piece of code!

An `ast` is useful in that it parses the code for you, in a place that you can actually work with it.

## Searching for a certain element

What if you were wondering, okay what are all the things imported in my file(s)?

An AST can help you answer this!

```bash
python ex2_ast_visit_imports.py ex2_lots_of_imports.py
```

If you look at the code, you may notice that ASTs use the "Visitor" design pattern. By subclassing the "NodeVisitor" class and specify what sorts of things to visit, you can define your own behavior upon visiting that sort of node.

## Using the AST to inform your refactoring

....
