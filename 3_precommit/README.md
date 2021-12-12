# Pre-commit

## What is `pre-commit`?

`pre-commit` is a tool that will run checks or formatters on your code during the git commit. `pre-commit` hooks will both refactor your code, and then ensure that old patterns won't creep back in!

## What should I use?

There's not much code in this section. This is just a place for me to share my favorite python `pre-commit` hooks! All these are great

1. [pygrep](https://pre-commit.com/#pygrep)
    - search for any regex in your code
        - comes bundled with pre-commit
    - there's also a [pygrep-hook](https://github.com/pre-commit/pygrep-hooks) repo with free pygreps to borrow
2. opinionated code formatters
    - [Python black](https://github.com/psf/black)
    - [Prettier](https://prettier.io/)
3. remove old syntax
    - [pyupgrade](https://github.com/asottile/pyupgrade/)
    - [react codemods](https://github.com/reactjs/react-codemod/)
        - not available via pre-commit, but excellent nonetheless
4. sort your imports
    - [isort](https://github.com/PyCQA/isort)
    - alternatively, [reorder_python_imports](https://github.com/asottile/reorder_python_imports)
5. [mypy](https://github.com/python/mypy/)
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
-   repo: https://github.com/asottile/pyupgrade
    rev: v2.26.0
    hooks:
    -   id: pyupgrade
        # pyupgrade works best if you give a minimum python version
        args: [--py36-plus]
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.910
    hooks:
    -   id: mypy
        # it can be useful to not type-check your tests
        exclude: ^tests/
-   repo: https://github.com/pycqa/isort
    rev: 5.9.3
    hooks:
      - id: isort
        name: isort
```

## Useful commands

- `pre-commit autoupdate` -- update all hooks
- `pre-commit run black --all-files` -- run the `black` hook on everything
- `pre-commit run black --files my_folder/` -- run the `black` hook on one folder
