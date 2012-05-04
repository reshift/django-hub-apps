
from django.contrib import admin
from django.db.models import AutoField
from django.forms import ValidationError
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from copy import deepcopy

from hub.core.models import CONTENT_STATUS_PUBLISHED

class CoreAdmin(admin.ModelAdmin):
    extra_fieldsets = None

    def __init__(self, *args, **kwargs):
        """
        For ``Page`` subclasses that are registered with an Admin class
        that doesn't implement fieldsets, add any extra model fields
        to this instance's fieldsets. This mimics Django's behaviour of
        adding all model fields when no fieldsets are defined on the
        Admin class.
        """
        super(CoreAdmin, self).__init__(*args, **kwargs)
        print self.extra_fieldsets
        if self.extra_fieldsets is not None:
            print "yo"
            self.fieldsets = deepcopy(self.fieldsets) + self.extra_fieldsets


class DisplayableAdmin(CoreAdmin):
    """
    Admin class for subclasses of the abstract ``Displayable`` model.
    """

    list_display = ("title", "status",)
    list_display_links = ("title",)
    #list_editable = ("status",)
    list_filter = ("status",)
    search_fields = ("title",)
    date_hierarchy = "publish_date"
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = (
        (None, {
            "fields": ["title", "slug", "status", "publish_date", "expiry_date",],
        }),
        (_("Meta data"), {
            "fields": [("meta_description",), "meta_keywords"],
            "classes": ("collapse-closed",)
        }),
    )