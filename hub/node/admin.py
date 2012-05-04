
from django.contrib import admin
from django.db.models import AutoField
from django.forms import ValidationError
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from hub.node.models import Node
from hub.core.admin import DisplayableAdmin


#page_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
#page_fieldsets[0][1]["fields"] += (("in_navigation", "in_footer"), "login_required",)

class NodeAdmin(DisplayableAdmin):
    pass   