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

---------------
Register on PyPi
---------------
Follow `this link <http://peterdowns.com/posts/first-time-with-pypi.html>`_.

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
