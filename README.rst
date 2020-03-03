.. image:: https://travis-ci.org/supakeen/steck.svg?branch=master
    :target: https://travis-ci.org/supakeen/steck

.. image:: https://readthedocs.org/projects/steck/badge/?version=latest
    :target: https://steck.readthedocs.io/en/latest/

.. image:: https://steck.readthedocs.io/en/latest/_static/license.svg
    :target: https://github.com/supakeen/steck/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. image:: https://img.shields.io/pypi/v/steck
    :target: https://pypi.org/project/steck

.. image:: https://codecov.io/gh/supakeen/steck/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/supakeen/steck

steck
#####

``steck`` is a Python application to interface with the pinnwand_ pastebin
software. By default ``steck`` pastes to bpaste_ but you can override the
instance used.

Prerequisites
=============
* Python >= 3.6
* click
* requests
* python-magic
* termcolor
* appdirs
* toml

Usage
=====

Simple use::

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

Skip the confirmation::

  € steck paste --no-confirm *
 
Don't try to guess at filetypes::

  € steck paste --no-magic *
 

More usecases are found in the documentation_.


Configuration
=============

The default argument values used by ``steck`` can be configured by copying the
``steck.toml-dist`` file to ``~/.config/steck/steck.toml``. You can turn off
the confirmation or choose another pinnwand instance there.

More about configuration can be found at the documentation_.

License
=======
``steck`` is distributed under the MIT license. See `LICENSE`
for details.

.. _bpaste: https://bpaste.net/
.. _project page: https://github.com/supakeen/steck
.. _documentation: https://steck.readthedocs.io/en/latest/
.. _pinnwand: https://supakeen.com/project/pinnwand
