# python-package-template

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Development environment

- [macOS 12.6.5](https://www.apple.com/tw/macos/monterey/)
- [Visual Studio Code 1.85.1](https://code.visualstudio.com/)
- [Python 3.11.7](https://www.python.org/)

## Official tutorial

- [Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## Export requirements.txt

```shell
$ pipenv requirements > requirements.txt

$ pipenv requirements --dev > dev-requirements.txt
```

## Build package

```shell
$ python -m build
```

## Package require files

```
.
├── dev-requirements.txt
├── dist (build)
│   ├── python_package_template-0.0.1-py3-none-any.whl
│   └── python_package_template-0.0.1.tar.gz
├── pyproject.toml
├── requirements.txt
└── src
    ├── python_package_template
    │   ├── __init__.py
    │   ├── example.py
    │   └── py.typed
    └── python_package_template.egg-info (build)
        ├── PKG-INFO
        ├── SOURCES.txt
        ├── dependency_links.txt
        └── top_level.txt
```

## Generate type stub files

- [Guide](https://typing.readthedocs.io/en/latest/guides/writing_stubs.html)

```shell
$ cd src
$ stubgen -p python_package_template -o typings
```

## Install package from other project

```shell
$ pip install git+https://github.com/billy0402/python-package-template.git

$ pipenv install git+https://github.com/billy0402/python-package-template.git

$ poetry add git+https://github.com/billy0402/python-package-template.git
```
