from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.


class Follow(models.Model):

    user_from = models.ForeignKey(
        get_user_model(),
        verbose_name=_("User"),
        related_name="user_from_set",
        on_delete=models.CASCADE,
    )
    user_to = models.ForeignKey(
        get_user_model(), verbose_name=_("Follower"), related_name="user_to_set", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("follow")
        verbose_name_plural = _("follows")
        unique_together = ("user_from", "user_to")

    def __str__(self):
        return f"{self.user_from.username} is following {self.user_to.username}"

    def get_absolute_url(self):
        return reverse("followers_list", kwargs={"username": self.user_to.username})


user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField(
    "self", through=Follow, related_name="followers", symmetrical=False, verbose_name=_("Following")))


class Profile(models.Model):

    user = models.OneToOneField(
        get_user_model(),
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="profile",
    )
    slug = models.SlugField(_("Slug"), blank=True)
    avatar = models.ImageField(
        _("Avatar"), upload_to="uploads/", null=True, blank=False)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("followers:user_profile", kwargs={"slug": self.slug})
