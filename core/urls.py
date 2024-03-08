from django.urls import path
from .views import UserAPIView, hello_world

urlpatterns = [
    path('hello/',hello_world,name='hello-world'),
    path('user/', UserAPIView.as_view(), name='user-list'),
]