#from .views import Drivers
from django.urls import path
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    DriverPofile,
    Login,
    ActiveLogin,ActiveDrivers,
    RideCreationView, getEarnings,
    RideHistory, NotificationView,
    UserViewSet,
    UpdateProfilePicView
    )


urlpatterns=[
    path('profile/',DriverPofile.as_view()),
    path('login/',Login.as_view()),
    path('active/', ActiveLogin.as_view()),
    path('active_drivers/',ActiveDrivers.as_view()),
    path('rides/',RideCreationView.as_view()),
    path('earnings/',getEarnings),
    path('history/',RideHistory.as_view()),
    path('alerts/',NotificationView.as_view()),
    path('alldriver/',UserViewSet.as_view({'get': 'list'})),
    path('image/',UpdateProfilePicView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
