# Generated by Django 4.0.1 on 2022-02-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_profile_site_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/'),
        ),
    ]
