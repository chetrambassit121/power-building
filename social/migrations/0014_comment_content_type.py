# Generated by Django 4.0.4 on 2022-05-12 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("social", "0013_remove_comment_content_type_remove_comment_object_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="content_type",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
    ]
