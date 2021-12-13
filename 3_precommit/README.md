# Pre-commit

## What is `pre-commit`?

`pre-commit` is a tool that will run checks or formatters on your code during the git commit. `pre-commit` hooks will both refactor your code, and then ensure that old patterns won't creep back in!

## What should I use?

There's not much code in this section. This is just a place for me to share my favorite `pre-commit` hooks! All these are great

1. [pygrep](https://pre-commit.com/#pygrep) (language-agnostic)
    - fail the commit if a certain string / pattern is found
        - comes bundled with pre-commit
    - there's also a [pygrep-hook](https://github.com/pre-commit/pygrep-hooks) repo with examples to borrow
2. opinionated code formatters
    - [black](https://github.com/psf/black) (python)
    - [Prettier](https://prettier.io/) (javascript / typescript)
3. remove old syntax
    - [pyupgrade](https://github.com/asottile/pyupgrade/) (python)
    - [codemods](https://github.com/reactjs/react-codemod/) (react)
        - codemods are not available via pre-commit, but excellent nonetheless
4. sort your imports
    - [isort](https://github.com/PyCQA/isort) (python)
    - alternatively, [reorder_python_imports](https://github.com/asottile/reorder_python_imports) (python)
5. [mypy](https://github.com/python/mypy/) (python)
    - enforce your type checking

## How to set up

Add a `pre-commit-config.yaml` file in your repo. Control your hooks via this config. It should look like this...

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
```

Then run `pre-commit install` and you're done!

## Useful commands

- `pre-commit autoupdate` -- update all hooks
- `pre-commit run black --all-files` -- run the `black` hook on everything
- `pre-commit run black --files my_folder/` -- run the `black` hook on one folder
