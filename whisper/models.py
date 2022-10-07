from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Whisper(models.Model):

    user = models.ForeignKey(
        get_user_model(), verbose_name=_("User"), on_delete=models.CASCADE, related_name="whispers"
    )
    body = models.TextField(_("Body"))
    created_at = models.DateTimeField(_("Created"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now_add=True)

    class Meta:
        verbose_name = _("whisper")
        verbose_name_plural = _("whispers")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user}'s whisper"


class Like(models.Model):

    user = models.ForeignKey(get_user_model(), verbose_name=_(
        "likes"), related_name="likes", on_delete=models.CASCADE)
    whisper = models.ForeignKey(Whisper, verbose_name=_(
        "likes"), related_name="likes", on_delete=models.CASCADE)
    liked = models.BooleanField(_("Liked"))

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        if self.liked:
            return f"{self.user.username} likes a whisper"
        return f"{self.user.username} dislikes a whisper"
