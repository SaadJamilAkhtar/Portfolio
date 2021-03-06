# Generated by Django 4.0.1 on 2022-02-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/posts')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(default='Basic', max_length=25)),
                ('description', models.CharField(default='Lorem ipsum', max_length=255)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/images')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/clients')),
                ('testimonial', models.TextField()),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=255)),
                ('greeting', models.CharField(default='Hi, I am', max_length=255)),
                ('main_designation', models.CharField(default='Web Developer', max_length=255)),
                ('about', models.TextField()),
                ('cv', models.FileField(upload_to='media/documents/')),
                ('enable_services', models.BooleanField(default=True)),
                ('enable_pricing', models.BooleanField(default=True)),
                ('enable_testimonials', models.BooleanField(default=True)),
                ('enable_posts', models.BooleanField(default=True)),
                ('posts', models.ManyToManyField(to='User.Posts')),
                ('pricing', models.ManyToManyField(to='User.Pricing')),
                ('services', models.ManyToManyField(to='User.Services')),
                ('testimonials', models.ManyToManyField(to='User.Testimonials')),
            ],
        ),
    ]
