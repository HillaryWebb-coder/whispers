import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Activity


def create_activity(user, action, target=None):
    # Check if the action isn't being spammed
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)

    # Get existing similar activity only if the user hasn't created one in the last minute
    similar_actions = Activity.objects.filter(
        user=user, action=action, created__gte=last_minute)

    if target:
        # Check if user has an exixting activity
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct, target_id=target.id)

    if not similar_actions:
        # No existing activity found
        activity = Activity(user=user, action=action, target=target)
        activity.save()
        return True
    return False
