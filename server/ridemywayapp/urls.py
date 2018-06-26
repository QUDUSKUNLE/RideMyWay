from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from ridemywayapp import views

router = DefaultRouter()

router.register(r'api/users', views.UserViewSet)
router.register(r'api/offer-rides', views.OfferRidesViewSet)
router.register(r'api/request-rides', views.RequestRidesViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
