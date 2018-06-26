# Create your views here.
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import (
    OfferRidesSerializer,
    UserSerializer,
    RequestRidesSerializer,)
from .models import OfferRides, RequestRides


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                        permissions.IsAdminUser,)


class OfferRidesViewSet(viewsets.ModelViewSet):
    serializer_class = OfferRidesSerializer
    queryset = OfferRides.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestRidesViewSet(viewsets.ModelViewSet):
    serializer_class = RequestRidesSerializer
    queryset = RequestRides.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
