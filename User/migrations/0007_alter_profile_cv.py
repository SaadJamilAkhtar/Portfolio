# Generated by Django 4.0.1 on 2022-02-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_posts_image_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
