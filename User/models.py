from django.db import models


class Profile(models.Model):
    site_title = models.CharField(max_length=10, default='Idenify')
    name = models.CharField(max_length=255, default="John Doe")
    greeting = models.CharField(max_length=255, default="Hi!")
    main_designation = models.CharField(max_length=255, default="Web Developer")
    about = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='documents/', null=True, blank=True)
    enable_services = models.BooleanField(default=True)
    services = models.ManyToManyField('Services', blank=True)
    enable_pricing = models.BooleanField(default=True)
    pricing = models.ManyToManyField('Pricing', blank=True)
    enable_testimonials = models.BooleanField(default=True)
    testimonials = models.ManyToManyField("Testimonials", blank=True)
    enable_posts = models.BooleanField(default=True)
    posts = models.ManyToManyField('Posts', blank=True)
    linkedin = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/profile', null=True, blank=True)


class Testimonials(models.Model):
    image = models.ImageField(upload_to='images/clients')
    testimonial = models.TextField()
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Testimonials"


class Pricing(models.Model):
    plan_name = models.CharField(max_length=25, default="Basic")
    description = models.CharField(max_length=255, default="Lorem ipsum")
    price = models.FloatField(default=0.0)


class Services(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/services')

    class Meta:
        verbose_name_plural = "Services"


class Posts(models.Model):
    image = models.ImageField(upload_to='images/posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Posts"
