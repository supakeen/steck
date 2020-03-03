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
software.

Prerequisites
=============
* Python >= 3.6
* click
* requests
* python-magic
* termcolor

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
  View Paste https://localhost:8000/6MZA
  Remove Paste https://localhost:8000/remove/XFVRNNCC7L5ATXOU4RHZNBEKIQ


License
=======
``steck`` is distributed under the MIT license. See `LICENSE`
for details.

.. _project page: https://github.com/supakeen/steck
.. _documentation: https://steck.readthedocs.io/en/latest/
.. _pinnwand: https://supakeen.com/project/pinnwand
