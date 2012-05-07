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

2. Run ``./manage.py syncdb categories`` (or ``./manage.py migrate <app>`` if you are using `South <http://south.aeracode.org/>`_)

Models
=========================

SETTINGS
=========================

``CATEGORY_MODEL``
----------------------------------

The default category model.

Default: ``hub.categories.defaults.category.Category``

