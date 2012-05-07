from django import forms
from django.conf import settings

class TinyMceWidget(forms.Textarea):
  """
  Setup the JS files and targetting CSS class for a textarea to
  use TinyMCE.
  """

  class Media:
    js = ("tinymce/jscripts/tiny_mce/tiny_mce.js",
          settings.TINYMCE_JS_URL,)

  def __init__(self, *args, **kwargs):
    super(TinyMceWidget, self).__init__(*args, **kwargs)
    self.attrs["class"] = "mceEditor"