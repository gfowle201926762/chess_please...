# Generated by Django 4.1 on 2022-08-18 21:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0003_userprofile_followers_userprofile_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="challengers",
            field=models.ManyToManyField(
                blank=True, related_name="challengers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="challenging",
            field=models.ManyToManyField(
                blank=True, related_name="challenging", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
