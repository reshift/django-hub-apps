============
Installation
============

To use the hub apps
=========================

1. Install django-hub-apps::

    pip install https://github.com/hub-nl/django-hub-apps/zipball/master

2. Add the desired apps to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "hub.core",
           "hub.node",
           "hub.categories",
       ]

3. Run ``./manage.py syncdb`` (or ``./manage.py migrate <app>`` if you are using `South <http://south.aeracode.org/>`_)