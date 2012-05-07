============
Node
============

Installation
=========================

1. Add "hub.node" to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "hub.core",
           "hub.node",
       ]

Models
=========================

Node
----------------------------------
``hub.node.models.Node``

An abstract model consisting of the Orderable and Displayable models to provide some basic content(page) model
Features:

  * Orderable features
  * Displayable features
  * Auto-generated slug from the title.

