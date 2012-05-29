============
Categories
============

Installation
=========================

1. Add "hub.categories" to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "hub.core",
           "hub.categories",
       ]

2. Run ``./manage.py syncdb``

Models
=========================

CategoryBase
----------------------------------
``hub.categories.bases.CategoryBase``

Abstract model providing category basics

Category
----------------------------------
``hub.categories.defaults.category.Category``

Settings
=========================

``CATEGORY_MODEL``
----------------------------------

The default category model.

Default: ``hub.categories.defaults.category.Category``