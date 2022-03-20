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
    enable_portfolio = models.BooleanField(default=True)
    portfolio = models.ManyToManyField('Portfolio', blank=True, null=True)


class Testimonials(models.Model):
    image = models.ImageField(upload_to='images/clients')
    testimonial = models.TextField()
    name = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        super(Testimonials, self).save(*args, **kwargs)
        profile = Profile.objects.first()
        profile.testimonials.add(self)
        profile.save()

    def __str__(self):
        return str(self.name) + "'s Testimonial"

    class Meta:
        verbose_name_plural = "Testimonials"


class Pricing(models.Model):
    plan_name = models.CharField(max_length=25, default="Basic")
    description = models.TextField(default="Lorem ipsum")
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.plan_name)

    def save(self, *args, **kwargs):
        super(Pricing, self).save(*args, **kwargs)
        profile = Profile.objects.first()
        profile.pricing.add(self)
        profile.save()


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/services')

    def __str__(self):
        return "Service - " + str(self.name)

    def save(self, *args, **kwargs):
        super(Services, self).save(*args, **kwargs)
        profile = Profile.objects.first()
        profile.services.add(self)
        profile.save()

    class Meta:
        verbose_name_plural = "Services"


class Posts(models.Model):
    image = models.ImageField(upload_to='images/posts')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def save(self, *args, **kwargs):
        super(Posts, self).save(*args, **kwargs)
        profile = Profile.objects.first()
        profile.posts.add(self)
        profile.save()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Posts"


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/portfolio')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        super(Portfolio, self).save(*args, **kwargs)
        profile = Profile.objects.first()
        profile.portfolio.add(self)
        profile.save()

    def __str__(self):
        return str(self.title) + " - " + str(self.category)


class Settings(models.Model):
    host_list = [('smtp.gmail.com', 'gmail'), ('smtp-mail.outlook.com', 'outlook')]
    port_list = [(587, 'gmail'), (587, 'outlook')]
    from_email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    to_email = models.EmailField(blank=True, null=True)
    host = models.CharField(max_length=255, choices=host_list, default='smtp.gmail.com')
    port = models.PositiveIntegerField(choices=port_list, default=587)

    class Meta:
        verbose_name_plural = 'Settings'
