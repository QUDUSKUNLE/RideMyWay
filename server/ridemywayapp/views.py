# Create your views here.
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import permissions, generics
from django.contrib.auth.models import User
from .serializers import (
    OfferRidesSerializer,
    UserSerializer,
    RequestRidesSerializer,)
from .models import OfferRides, RequestRides


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse(
            'user-list', request=request, format=format),
        'offer-rides': reverse(
            'offer-rides-list', request=request, format=format),
        'request-rides': reverse(
            'request-rides-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):

    """
        Class UserList serializer
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UserDetail(generics.RetrieveAPIView):

    """
        Class UserDetail serializer
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class OfferRidesList(generics.ListCreateAPIView):

    """
        Class OfferRidesList serializer
    """

    serializer_class = OfferRidesSerializer
    queryset = OfferRides.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OfferRidesDetail(generics.RetrieveUpdateDestroyAPIView):

    """
        Class OfferRidesDetail serializer
    """

    serializer_class = OfferRidesSerializer
    queryset = OfferRides.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RequestRidesList(generics.ListCreateAPIView):

    """
        Class OfferRidesDetail serializer
    """

    serializer_class = RequestRidesSerializer
    queryset = RequestRides.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class RequestRidesDetails(generics.RetrieveUpdateDestroyAPIView):

    """
        Class OfferRidesDetail serializer
    """

    serializer_class = RequestRidesSerializer
    queryset = RequestRides.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
