============
Overview
============

1. Install django-hub-apps::

    pip install https://github.com/hub-nl/django-hub-apps/zipball/master

2. Add the "hub.core" to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "hub.core",
       ]

Models
=========================

Displayable
----------------------------------
``hub.core.models.Displayable``

Abstract model that provides features of a visible page on the
website such as publishing fields.

RichText
----------------------------------
``hub.core.models.RichText``

Provides a Rich Text field for managing general content.

Featurable
----------------------------------
``hub.core.models.Featurable``

Abstract feature model

Settings
=========================

``RICHTEXT_WIDGET_CLASS``
----------------------------------

The default widget to be used for richtext

Default: ``hub.core.forms.TinyMceWidget``