# Generated by Django 4.1.1 on 2022-09-28 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whisper', '0002_whisper_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whisper',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whispers', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]