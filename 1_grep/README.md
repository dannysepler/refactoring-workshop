# `grep`

## Introduction

`grep` is a powerful tool to find things in your code.

`grep` finds all lines that match a given regular expresion and streams them to your output.


## Getting Started

Let's start with a simple example: where's waldo! Rather... where's Harry?

I've pasted the first 50 pages of Harry Potter into this folder. Let's find how many times the name Harry was mentioned.

Here, let's try:

```bash
grep Harry ex1_harry.txt
```

## Excluding Results

If you look at the results, you may notice something. We're getting tons of mentions of 'Harry', but we're also getting every page number! Let's remove those.

Luckily with `grep` it's a stream, so we can use pipes!

```bash
grep Harry ex1_harry.txt | grep -v "Page |"
```

Here we're saying, find me all the lines that match "Harry", then remove all the lines that match "Page |"

## Using regex in `grep`

Owls are a big theme in Harry Potter 🦉 -- let's find some!

```bash
grep owl ex1_harry.txt
```

You may notice a few `owl` results here, but something unexpected occurred. We see `J.K. Rowling` far more often!

A naive fix here would be to look for owl with spaces before and after, like so:

```bash
grep ' owl ' ex1_harry.txt
```

But now you're missing a few results, such as `owls`. This is where grep begins to shine, as opposed to an IDE search! Let's use `regex` to come up with a better query.

```bash
grep -E ' owl(s?) ' ex1_harry.txt
```

Pop quiz: one hard thing to search for is `owl-free`. How can we do that?

## Are there good `grep` tools out there?

Sure are!

1. `git grep` is much faster and prettier than grep.
2. The [silver searcher](https://github.com/ggreer/the_silver_searcher) is also much faster and prettier than grep (but it's mac-only).
