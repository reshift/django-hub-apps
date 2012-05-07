# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

#==============================================================================
# Get the category model
#==============================================================================
CATEGORY_MODEL = getattr(settings, 'CATEGORY_MODEL', 'hub.categories.defaults.category.Category')
Category = load_class(CATEGORY_MODEL)