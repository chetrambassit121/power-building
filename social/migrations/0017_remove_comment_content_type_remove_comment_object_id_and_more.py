# Generated by Django 4.0.4 on 2022-05-12 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0016_remove_comment_post"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="content_type",),
        migrations.RemoveField(model_name="comment", name="object_id",),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                to="social.post",
            ),
        ),
    ]
