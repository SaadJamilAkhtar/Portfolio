# Generated by Django 4.0.1 on 2022-02-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_pricing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
