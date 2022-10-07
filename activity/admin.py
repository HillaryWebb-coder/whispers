from django.contrib import admin
from .models import Activity
# Register your models here.


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('action',)
