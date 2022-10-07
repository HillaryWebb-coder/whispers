from django.apps import AppConfig


class FollowersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "followers"

    def ready(self) -> None:
        from . import signals
        return super().ready()
