from django.urls import path
from . import views
from .views import (
    LockerDetailView
)

urlpatterns = [
    path('', views.home, name='inpro-home'),
    path('locker/<int:pk>', LockerDetailView.as_view(), name='locker-detail')
]
