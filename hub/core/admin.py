
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
        super(CoreAdmin, self).__init__(*args, **kwargs)
        if self.extra_fieldsets is not None:
            self.fieldsets = deepcopy(self.fieldsets) + self.extra_fieldsets

        self.fieldsets = deepcopy(self.fieldsets)
        for field in reversed(self.model._meta.fields):
            #if field not in Page._meta.fields and field.name != "page_ptr":
            print field
            if field is not None:
                self.fieldsets[0][1]["fields"].insert(3, field.name)

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