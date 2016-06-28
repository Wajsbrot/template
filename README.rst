================
Template project
================

Create an empty python package following the conventions of `pytest <http://pytest.org/latest/goodpractices.html#goodpractices>`.
This README follows the `REST <http://www.sphinx-doc.org/en/stable/rest.html>` text convention such that documentation can be created with Sphinx.

Test package with ``pip install -e .``::

---------------
Register on PyPi
---------------
Follow `this link <http://peterdowns.com/posts/first-time-with-pypi.html>`.

-----------------
Requirements file
-----------------
This is a way to define the requirements of the complete python environment.
Consider updating the **install_requires** field of setup.py instead.

To get all dependencies: ``pip freeze > requirements.txt``
Install required packages: ``pip install -r requirements.txt``
