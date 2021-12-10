# `sed`

`sed` is a find-and-replace tool to help you refactor broad swaths of code.

`sed` stands for stream editor.

## Getting Started

Let's take a simple example, `ex1_func.py`. We have this lovely little file, but here's the thing. Corporate told us to find kangaroos, not koalas. Oh no!

Luckily with sed, we can rename all mentions of koalas to kangaroos. Let's give it a shot.

```bash
sed -i 's/koala/kangaroo/g' ex1_func.py
```
