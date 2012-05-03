
from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models
from django.db.models.base import ModelBase
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings

from hub.core.managers import *
from hub.core.fields import RichTextField

from taggit.managers import TaggableManager
from autoslug import AutoSlugField

class MetaData(models.Model):
    """
    Abstract model that provides meta data for content.
    """

    meta_description = models.TextField(_("Description"), blank=True)
    meta_keywords = models.CharField(max_length=255, verbose_name=_("Keywords"))

    class Meta:
      abstract = True

    def save(self, *args, **kwargs):
      """
      Set the description field on save.
      """
      if self.meta_description == "":
        self.meta_description = strip_tags(self.meta_description_from_content())
      super(MetaData, self).save(*args, **kwargs)

    def description_from_content(self):
        """
        Returns the first block or sentence of the first content-like
        field.
        """
        description = ""
        # Use the first RichTextField, or TextField if none found.
        for field_type in (RichTextField, models.TextField):
            if not description:
                for field in self._meta.fields:
                    if isinstance(field, field_type) and \
                        field.name != "description":
                        description = getattr(self, field.name)
                        if description:
                            break
        # Fall back to the title if description couldn't be determined.
        if not description:
            description = unicode(self)
        # Strip everything after the first block or sentence.
        ends = ("</p>", "<br />", "<br/>", "<br>", "</ul>",
                "\n", ". ", "! ", "? ")
        for end in ends:
            pos = description.lower().find(end)
            if pos > -1:
                description = TagCloser(description[:pos]).html
                break
        else:
            description = truncatewords_html(description, 100)
        return description

CONTENT_STATUS_DRAFT = 1
CONTENT_STATUS_PUBLISHED = 2
CONTENT_STATUS_CHOICES = (
    (CONTENT_STATUS_DRAFT, _("Draft")),
    (CONTENT_STATUS_PUBLISHED, _("Published")),
)

class Featurable(models.Model):
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

class Displayable(MetaData):
    """
    Abstract model that provides features of a visible page on the
    website such as publishing fields.
    """

    status = models.IntegerField(_("Status"), 
        choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED)
    publish_date = models.DateTimeField(_("Published from"),
        help_text=_("With published checked, won't be shown until this time"),
        blank=True, null=True)
    expiry_date = models.DateTimeField(_("Expires on"),
        help_text=_("With published checked, won't be shown after this time"),
        blank=True, null=True)

    objects = DisplayableManager()
    search_fields = {"keywords": 10, "title": 5}

    class Meta:
      abstract = True

    def save(self, *args, **kwargs):
      """
      Set default for ``publish_date``. We can't use ``auto_add`` on
      the field as it will be blank when a blog post is created from
      the quick blog form in the admin dashboard.
      """
      if self.publish_date is None:
          self.publish_date = now()
      super(Displayable, self).save(*args, **kwargs)

class RichText(models.Model):
  """
  Provides a Rich Text field for managing general content and making
  it searchable.
  """

  body = RichTextField(_("Content"))

  search_fields = ("body",)

  class Meta:
    abstract = True