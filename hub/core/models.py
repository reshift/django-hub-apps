
from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models
from django.db.models.base import ModelBase
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from django.utils.html import strip_tags
from datetime import *

from hub.core.managers import *
from hub.core.fields import RichTextField

from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

class Featurable(models.Model):
  """
  Abstract feature model
  """

  featured   = models.BooleanField(default=False, verbose_name='Featured')

  class Meta:
      abstract = True

  def admin_is_featured(self):
    if self.featured == True:
      return '<img src="%sgrappelli/img/admin/icon-yes.gif"/>' % settings.STATIC_URL
    if self.featured == False:
      return '<img src="%sgrappelli/img/admin/icon-no.gif"/>' % settings.STATIC_URL

  admin_is_featured.short_description = 'Featured?'
  admin_is_featured.allow_tags = True    

CONTENT_STATUS_DRAFT = 1
CONTENT_STATUS_PUBLISHED = 2
CONTENT_STATUS_CHOICES = (
    (CONTENT_STATUS_DRAFT, _("Draft")),
    (CONTENT_STATUS_PUBLISHED, _("Published")),
)

class Displayable(models.Model):
    """
    Abstract model that provides features of a visible page on the
    website such as publishing fields.
    """

    status = models.IntegerField(_("Status"), 
        choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED)
    publish_date = models.DateTimeField(_("Published from"),
        help_text=_("With published checked, won't be shown until this time"),
        default=datetime.now())
    expiry_date = models.DateTimeField(_("Expires on"),
        help_text=_("With published checked, won't be shown after this time"),
        blank=True, null=True)

    objects = DisplayableManager()
    search_fields = {"title": 5,}

    class Meta:
      abstract = True

class Orderable(MPTTModel):
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

  tree = TreeManager()

  class Meta:
    abstract = True

class RichText(models.Model):
  """
  Provides a Rich Text field for managing general content and making
  it searchable.
  """

  body = RichTextField(_("Content"))

  search_fields = ("body",)

  class Meta:
    abstract = True