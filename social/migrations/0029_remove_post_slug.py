# Generated by Django 3.2.13 on 2022-07-12 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0028_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
