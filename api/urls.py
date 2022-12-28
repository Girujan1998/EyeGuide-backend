from django.urls import path

from . import views

urlpatterns = [
    path('get-gps', views.GPSView.as_view()),
    path('post-gps', views.GPSView.as_view())
]