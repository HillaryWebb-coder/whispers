# Generated by Django 4.1.1 on 2022-09-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Slug'),
        ),
    ]
