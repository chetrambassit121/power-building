# Generated by Django 4.0.4 on 2022-05-12 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_comment_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
