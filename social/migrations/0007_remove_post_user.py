# Generated by Django 4.0.4 on 2022-05-10 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]