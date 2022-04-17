# Generated by Django 4.0.4 on 2022-04-16 13:42

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_userprofile_pinterest_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast_Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'BroadCast Email to all Member',
                'verbose_name_plural': 'BroadCast Email',
            },
        ),
    ]
