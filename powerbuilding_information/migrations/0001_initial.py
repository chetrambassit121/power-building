# Generated by Django 4.0.4 on 2022-04-22 00:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "extra_info",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "dislikes",
                    models.ManyToManyField(
                        blank=True, related_name="dislikes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
