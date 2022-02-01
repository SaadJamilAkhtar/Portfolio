from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255, default="John Doe")
    greeting = models.CharField(max_length=255, default="Hi, I am")
    main_designation = models.CharField(max_length=255, default="Web Developer")
    about = models.TextField()
    cv = models.FileField(upload_to='media/documents/')


class Blogs(models.Model):
    pass
