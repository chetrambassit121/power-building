# Generated by Django 3.2.13 on 2022-06-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0027_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]