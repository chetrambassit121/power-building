# Generated by Django 4.0.4 on 2022-04-24 15:35

from django.db import migrations, models
import social.validators


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_delete_video_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/uploads/message_photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/uploads/post_photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='images/uploads/post_videos', validators=[social.validators.file_size]),
        ),
    ]
