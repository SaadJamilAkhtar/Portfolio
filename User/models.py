from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255, default="John Doe")
    greeting = models.CharField(max_length=255, default="Hi, I am")
    main_designation = models.CharField(max_length=255, default="Web Developer")
    about = models.TextField()
    cv = models.FileField(upload_to='media/documents/')
    enable_services = models.BooleanField(default=True)
    services = models.ManyToManyField('Services')
    enable_pricing = models.BooleanField(default=True)
    pricing = models.ManyToManyField('Pricing')


class Pricing(models.Model):
    pass


class Services(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images')


class Blogs(models.Model):
    pass
