from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def hello_world(request):
    user = User.objects.all().values()
    return HttpResponse(user)
