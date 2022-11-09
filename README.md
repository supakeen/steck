![steck logo, a polarbear opening a shirt like superman](https://src.tty.cat/supakeen/steck/raw/branch/master/doc/_static/logo-doc.png)

steck
#####

![rtd badge](https://readthedocs.org/projects/steck/badge/?version=latest) ![license badge](https://steck.readthedocs.io/en/latest/_static/license.svg) ![black badge](https://img.shields.io/badge/code%20style-black-000000.svg)

## About

``steck`` is a Python application to interface with the [pinnwand](https://github.com/supakeen/pinnwand) pastebin
software. By default ``steck`` pastes to [bpaste](https://bpa.st) but you can override the
instance used.

## Prerequisites

* Python >= 3.6
* click
* requests
* python-magic
* termcolor
* appdirs
* toml

## Usage

Simple use::

```
  € steck paste *      
  You are about to paste the following 7 files. Do you want to continue?
   - LICENSE
   - mypy.ini
   - poetry.lock
   - pyproject.toml
   - README.rst
   - requirements.txt
   - steck.py
  
  Continue? [y/N] y
  
  Completed paste.
  View link:    https://localhost:8000/W5
  Removal link: https://localhost:8000/remove/TS2AFFIEHEWUBUV5HLKNAUZFEI
```

You can also paste from stdin (a single file)::

```
  € steck paste --no-confirm -
```

Skip the confirmation::

```
  € steck paste --no-confirm *
```
 
Don't try to guess at filetypes::

```
  € steck paste --no-magic *
```
 
Skip checking files against ``.gitignore``::

```
  € steck paste --no-ignore *
```

Descend recursively::

```
  € steck paste **/*
```

More usecases are found in the [documentation](https://steck.readthedocs.io/en/latest/).


## Configuration

The default argument values used by ``steck`` can be configured by copying the
``steck.toml-dist`` file to ``~/.config/steck/steck.toml``. You can turn off
the confirmation or choose another pinnwand instance there.

More about configuration can be found at the [documentation](https://steck.readthedocs.io/en/latest/).

## License
``steck`` is distributed under the MIT license. See `LICENSE`
for details.
