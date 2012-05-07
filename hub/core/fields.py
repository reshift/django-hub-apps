
from bleach import clean
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hub import settings
from djutils.utils.helpers import load_class

from hub.utils.importing import import_dotted_path

class RichTextField(models.TextField):
  """
  TextField that stores HTML.
  """

  def formfield(self, **kwargs):
      """
      Apply the widget class defined by the
      ``RICHTEXT_WIDGET_CLASS`` setting.
      """
      try:
          widget_class = load_class(settings.RICHTEXT_WIDGET_CLASS)
      except ImportError:
          raise ImproperlyConfigured(_("Could not import the value of "
                                       "settings.RICHTEXT_WIDGET_CLASS: %s"
                                       % settings.RICHTEXT_WIDGET_CLASS))
      kwargs["widget"] = widget_class()
      formfield = super(RichTextField, self).formfield(**kwargs)
      return formfield

  def clean(self, value, model_instance):
    """
    Remove potentially dangerous HTML tags and attributes.
    """
    return clean(value, settings.RICHTEXT_ALLOWED_TAGS, settings.RICHTEXT_ALLOWED_ATTRIBUTES)