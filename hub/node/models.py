from django.core.urlresolvers import resolve, reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import *

from hub.core.models import Displayable, Orderable, RichText

from autoslug import AutoSlugField
from taggit.managers import TaggableManager

class Node(Displayable, Orderable):
  title      = models.CharField(max_length=255)
  slug       = AutoSlugField(populate_from='title', max_length=255, editable=True, blank=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
  updated_at = models.DateTimeField(auto_now=True)

  # Taggit
  tags = TaggableManager()

  def __unicode__(self):
    return self.title

  # MPTTMeta  
  class MPTTMeta:
    order_insertion_by = ['title']

  # Grapelli autocomplete label
  def related_label(self):
    return u"%s" % (self.title)

  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "title__icontains",)
  
  class Meta:
    abstract = True
    ordering = ('title', )