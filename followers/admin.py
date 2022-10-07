from django.contrib import admin

# Register your models here.
from .models import Follow, Profile


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("user_from", "user_to")
    search_fields = ("user_from", "user_to")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user",)
