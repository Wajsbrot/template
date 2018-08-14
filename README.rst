.. -*- mode: rst -*-

|Python36|_

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://badge.fury.io/py/scikit-learn


================
Template project
================

Create an empty python package following the conventions of `pytest <http://pytest.org/latest/goodpractices.html#goodpractices>`_.
This README follows the `REST <http://www.sphinx-doc.org/en/stable/rest.html>`_ text convention such that documentation can be created with Sphinx.

Test package with ``pip install -e .``

-----------------------
Publish package on PyPi
-----------------------

The config requires a .pypirc file in your home folder with the following content:

::
    [distutils]
    index-servers = pypi

    [pypi]
    repository: https://pypi.python.org/pypi
    username: wajsbrot
    password:

The package can be pushed with ``python setup.py sdist upload`` from the root directory of the project.

----------------------------
Test coverage with Coveralls
----------------------------

For local test coverage report install pytest-cov (``pip install pytest-cov``), then
run ``py.test --cov . --cov-report html && open htmlcov/index.html`` from the package root directory.

In order to use `coveralls <https://github.com/coveralls-clients/coveralls-python>`_ for automated test reporting   run ``coverage run --source=mypkg setup.py test && coveralls``

-----------------
Requirements file
-----------------

This is a way to define the requirements of the complete python environment.
Consider updating the **install_requires** field of setup.py instead.

To get all dependencies: 
:: 
  pip freeze > requirements.txt
  
Get only necessary dependencies (install pipreqs with ``pip install pipreqs``):
:: 
  pipreqs . > requirements.txt 

Install required packages:
::
  pip install -r requirements.txt
