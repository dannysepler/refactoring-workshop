# `sed`

## Introduction

`sed` is a find-and-replace tool to help you refactor broad swaths of code.

`sed` stands for stream editor. Let me first say, `sed` is VERY complicated and I'll only be giving a shallow understanding of it. A much more comprehensive tutorial [like this one](https://www.grymoire.com/Unix/Sed.html) would be much better for eager learners.

## Getting Started

Let's take a simple example, `ex1_func.py`. We have this lovely little file, but here's the thing. Corporate told us to find kangaroos, not koalas. Oh no!

Luckily with sed, we can rename all mentions of koalas to kangaroos. Let's give it a shot.

```bash
sed -i '' -e 's/koala/kangaroo/g' ex1_func.py
```

That was easy!

## What's going on here?

The `s` part means substitute, then we have a few delimiters, then the `g` flag for global. In between the delimiters are the string to replace, and the string to replace it with.

The delimiters (`/`) are arbitrary. The following all works:

```bash
sed -i '' -e 's,koala,kangaroo,g' ex1_func.py
sed -i '' -e 's*koala*kangaroo*g' ex1_func.py
```

Also note that `sed` uses regex to do its matching, so this works as well!

```bash
sed -i '' -e 's/koa.a/kangaroo/g' ex1_func.py
```

## Using `sed` to delete lines

Let's take a more concrete example from python. In py2, there were lines that were imported, that are no longer needed in py3.

If you look at `ex2_legacy_imports.py`, you may notice that the first three lines are no longer necessary in a py3 context. Let's remove 'em.

```bash
sed -i '' -e '/^from __future__/d' ex2_legacy_imports.py
```

Here, rather than using a substitute command, we're using a `/d` delete command, and matching all lines that start with (`^`) the string `from __future__`

Pop quiz: Can you remove all the page numbers from the Harry Potter file?

## A bulk rename

This is all well and good, but it's hard to appreciate how powerful `sed` is in these small files.

Let's go back to Harry Potter. I always thought Draco would have been a better main character than Harry, don't you think?

```bash
sed -i '' -e 's/Harry/Draco/g' ../1_grep/ex1_harry.txt
```

How fast was that? This is especially powerful in a large file with unknown quantities of things to rename!

## `sed` is complicated. That's okay!

When using `sed` it can be overwhelming how many options are available. The linked
tutorial is [huuuuuge](https://www.grymoire.com/Unix/Sed.html)! Don't let this
overwhelm you. Nobody knows all of `sed`. (And if someone does, ... ew.)

The important thing with `sed` is realizing that you're doing something manual over
and over, where a command can do it for you.

If you're doing any of the following, I hope a red flag pops up!

- renaming a variable across a folder
- changing a function call
- removing a line that matches a given pattern
- upgrading syntax when bumping some dependency
