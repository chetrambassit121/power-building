# Generated by Django 3.2.13 on 2022-05-19 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0021_auto_20220519_1908"),
    ]

    operations = [
        migrations.RenameField(
            model_name="posttest", old_name="slugtest", new_name="slug",
        ),
    ]
