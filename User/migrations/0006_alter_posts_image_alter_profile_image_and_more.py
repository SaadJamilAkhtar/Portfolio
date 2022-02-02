# Generated by Django 4.0.1 on 2022-02-02 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='images/posts'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='images/services'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(upload_to='images/clients'),
        ),
    ]
