from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Activity(models.Model):

    user = models.ForeignKey(get_user_model(), verbose_name=_(
        "User"), on_delete=models.CASCADE, db_index=True)
    action = models.CharField(_("Action"), max_length=200)
    target_ct = models.ForeignKey(ContentType, verbose_name=_(
        "Target Content Type"), blank=True, null=True, related_name="target_obj", on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(
        _("Target ID"), null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(
        _("Created"), auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.user} {self.action} {self.target}"
