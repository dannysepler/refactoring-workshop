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

## Analyzing your code

What if you were wondering, okay what are the most common things imported in my code?

An AST can help you answer this!

```bash
# analyze a file
python ex2_import_counter.py ex2_lots_of_imports.py

# or a whole folder
python ex2_import_counter.py ~/path/to/my/code
```

If you look at the code, you may notice that ASTs use the "Visitor" design pattern.
By subclassing the "NodeVisitor" class and specify what sorts of things to visit,
you can define your own behavior upon visiting that sort of node.

## Using the AST to inform your refactoring

Continuing the above example, let's say some import changed names. We can
rewrite every occurrence of this import, by using our knowledge of the AST
to reduce false positives

```bash
python ex3_rename_import.py ex2_lots_of_imports.py --before sys --after banana
```

/ Maybe your IDE does this already! If so, that's awesome, use that. But keep
this in mind, since maybe one day you will have some desired refactor that your
IDE doesn't handle for you.

**Pop quiz:**

1. If you read the code, how I handle the replacement is a little hacky. Why's that?

## Putting it all together

At this point, you may be thinking:

> Danny, you're so cool and knowledgeable! How do you know all this? Did you ever write a refactoring tool? What's your phone number?

Okay, maybe you didn't think _all_ of that. But yes! If you're curious
what a completed AST refactoring tool may look like, you can look at my
[pytestify](https://github.com/dannysepler/pytestify) package which uses these
concepts in practice.
