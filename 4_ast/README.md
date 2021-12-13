# The Abstract Syntax Tree

## Preface

Run `pip install astpretty` before using this section!

Also, while this section is written about python, the concepts are true of most code formatters in other languages. All languages have some sort of abstract syntax tree.

## Introduction

You may be wondering how a tool like `black` or `prettier` works. It's much more complicated than the simple refactors we've done with `sed`. It also seems to contain some knowledge of the python language. How is that?

The answer is that these tools know about Python's "Abstract Syntax Tree", or the
language's grammar / syntax.

## Viewing a file's AST

```bash
python ex1_print_ast.py ex1_simple_file.py
```

This prints out what Python sees when it looks at your file! You can use the AST
to draw conclusions from your code, or to make sweeping changes.

## Analyzing your code

Let's say you're wondering: what are the most common modules my code imports?

An AST can answer this!

```bash
# analyze a file
python ex2_import_counter.py ex2_lots_of_imports.py

# or a whole folder
python ex2_import_counter.py ~/path/to/my/code
```

You may notice that ASTs use the "visitor" design pattern. By subclassing the
`ast.NodeVisitor` class, you can define your own behavior for visiting each element.

## Using the AST to inform your refactoring

Let's say some import changed names. Using find-and-replace via `sed` or a
text editor may be overly sensitive, resulting in false positives. The AST
can help!

```bash
python ex3_rename_import.py ex2_lots_of_imports.py --before f --after banana
```

/ Maybe your IDE does this already! If so, that's awesome, use that. But keep
ASTs in mind, since one day you will need some refactor that your IDE doesn't
handle for you.

**Pop quiz:**

1. If you read the code, how I handle the replacement is a little hacky. Why's that?

## Putting it all together

At this point, you may be thinking:

> Danny, you're so cool and knowledgeable! How do you know all this? Did you ever write a refactoring tool? What's your phone number?

Okay, maybe you didn't think _all_ of that. But yes! If you're curious
what a completed AST refactoring tool may look like, you can look at my
[pytestify](https://github.com/dannysepler/pytestify) package which uses these
concepts in practice.
