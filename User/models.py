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
    enable_testimonials = models.BooleanField(default=True)
    testimonials = models.ManyToManyField("Testimonials")
    enable_posts = models.BooleanField(default=True)
    posts = models.ManyToManyField('Posts')


class Testimonials(models.Model):
    image = models.ImageField(upload_to='media/images/clients')
    testimonial = models.TextField()
    name = models.CharField(max_length=15)


class Pricing(models.Model):
    plan_name = models.CharField(max_length=25, default="Basic")
    description = models.CharField(max_length=255, default="Lorem ipsum")
    price = models.FloatField(default=0.0)


class Services(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images')


class Posts(models.Model):
    image = models.ImageField(upload_to='media/images/posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

