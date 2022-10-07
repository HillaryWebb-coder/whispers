from django.contrib import admin

from .models import Whisper, Like


@admin.register(Whisper)
class WhisperAdmin(admin.ModelAdmin):
    list_display = ("user", "body")
    list_filter = ("created_at", "updated_at")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "whisper")
