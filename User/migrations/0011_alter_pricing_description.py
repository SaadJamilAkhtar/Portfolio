# Generated by Django 4.0.1 on 2022-02-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_remove_portfolio_description_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='description',
            field=models.TextField(default='Lorem ipsum'),
        ),
    ]