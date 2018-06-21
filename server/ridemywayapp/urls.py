from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from ridemywayapp import views

router = DefaultRouter()

router.register(r'api/rides', views.RidesViewSet)
router.register(r'api/users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
