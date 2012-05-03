
from operator import ior, iand
from string import punctuation

from django.db.models import Manager, Q, CharField, TextField, get_models
from django.db.models.query import QuerySet

class PublishedManager(Manager):
    """
    Provides filter for restricting items returned by status and
    publish date when the given user is not a staff member.
    """

    def published(self, for_user=None):
        """
        For non-staff users, return items with a published status and
        whose publish and expiry dates fall before and after the
        current date when specified.
        """
        from hub.core.models import CONTENT_STATUS_PUBLISHED
        if for_user is not None and for_user.is_staff:
            return self.all()
        return self.filter(
            Q(publish_date__lte=now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=now()) | Q(expiry_date__isnull=True),
            Q(status=CONTENT_STATUS_PUBLISHED))

    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class DisplayableManager(PublishedManager):
    pass
