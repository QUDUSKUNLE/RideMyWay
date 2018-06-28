from django.conf.urls import url
from ridemywayapp import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^api/users/$',
        views.UserList.as_view(), name='user-list'),
    url(r'^api/offer-rides/$',
        views.OfferRidesList.as_view(), name='offer-rides-list'),
    url(r'^api/request-rides/$',
        views.RequestRidesList.as_view(), name='request-rides-list'),

    url(r'^api/users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(), name='user-detail'),
    url(r'^api/offer-rides/(?P<pk>[0-9]+)/$',
        views.OfferRidesDetail.as_view(), name='offer-rides-detail'),
    url(r'^api/request-rides/(?P<pk>[0-9]+)/$',
        views.RequestRidesDetails.as_view(), name='request-rides-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
