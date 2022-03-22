from User.models import *


def setup():
    users = Profile.objects.all()
    settings = Settings.objects.all()
    if users.count() == 0:
        Profile.objects.create()
    if settings.count() == 0:
        Settings.objects.create()
