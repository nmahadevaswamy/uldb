from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


def hello_world(request):
    user = User.objects.all().values()
    return HttpResponse(user)


class UserAPIView(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)