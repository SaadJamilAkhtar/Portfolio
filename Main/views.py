from django.shortcuts import render
from User.models import *


def index(request):
    users = Profile.objects.all()
    if users.count() == 0:
        Profile.objects.create()
    user = Profile.objects.first()

    data = {
        'user': user
    }

    return render(request, 'index.html', data)
