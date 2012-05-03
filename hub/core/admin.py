
from django.contrib import admin
from django.db.models import AutoField
from django.forms import ValidationError
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from hub.core.models import CONTENT_STATUS_PUBLISHED

class DisplayableAdmin(admin.ModelAdmin):
    """
    Admin class for subclasses of the abstract ``Displayable`` model.
    """

    list_display = ("title", "status", "admin_link")
    list_display_links = ("title",)
    #list_editable = ("status",)
    list_filter = ("status",)
    search_fields = ("title", "content",)
    date_hierarchy = "publish_date"
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = (
        (None, {
            "fields": ["title", "status", ("publish_date", "expiry_date")],
        }),
        (_("Meta data"), {
            "fields": ["slug", ("meta_description",), "meta_keywords"],
            "classes": ("collapse-closed",)
        }),
    )