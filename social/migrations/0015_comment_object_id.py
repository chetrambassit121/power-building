# Generated by Django 4.0.4 on 2022-05-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0014_comment_content_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="object_id",
            field=models.PositiveIntegerField(default=False),
        ),
    ]
