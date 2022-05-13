# Generated by Django 4.0.4 on 2022-05-11 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('social', '0007_remove_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(default=False),
        ),
    ]
