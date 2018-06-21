from django.shortcuts import render

# Create your views here.
from rest_framework import routers, viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import RidesSerializer, UserSerializer
from .models import Rides


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RidesViewSet(viewsets.ModelViewSet):
    serializer_class = RidesSerializer
    queryset = Rides.objects.all()
