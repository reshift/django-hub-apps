from django.conf import settings

RICHTEXT_WIDGET_CLASS	= getattr(settings, 'RICHTEXT_WIDGET_CLASS', 'hub.core.forms.TinyMceWidget')