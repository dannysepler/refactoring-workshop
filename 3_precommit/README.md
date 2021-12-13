# Pre-commit

## What is `pre-commit`?

`pre-commit` is a tool that will run checks or formatters on your code during the git commit. `pre-commit` hooks will both refactor your code, and then ensure that old patterns won't creep back in!

## What should I use?

There's not much code in this section. This is just a place for me to share my favorite `pre-commit` hooks! All these are great

1. fail a commit if a string is found
    - [pygrep](https://pre-commit.com/#pygrep) (language-agnostic)
        - comes bundled with pre-commit
    - see also [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks): a set of pygrep hooks maintained by pre-commit
2. code formatters
    - [black](https://github.com/psf/black) (python)
    - [Prettier](https://prettier.io/) (javascript / typescript)
3. remove old syntax
    - [pyupgrade](https://github.com/asottile/pyupgrade/) (python)
    - [codemods](https://github.com/reactjs/react-codemod/) (react)
        - codemods are not available via pre-commit, but excellent nonetheless
4. import sorting
    - [isort](https://github.com/PyCQA/isort) (python)
    - alternatively, [reorder_python_imports](https://github.com/asottile/reorder_python_imports) (python)
5. type checking
    - [mypy](https://github.com/python/mypy/) (python)

## How to set up

Add a `pre-commit-config.yaml` file in your repo. Control your hooks via this config. It should look like this...

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/pycqa/isort
    rev: 5.9.3
    hooks:
      - id: isort
```

Then run `pre-commit install` and you're done!

## Useful commands

- `pre-commit autoupdate` -- update all hooks
- `pre-commit run black --all-files` -- run the `black` hook on everything
- `pre-commit run black --files my_folder/` -- run the `black` hook on one folder
