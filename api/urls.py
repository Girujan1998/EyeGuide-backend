from django.urls import path

from . import views

urlpatterns = [
    path('get-gps', views.GPSView.as_view()),
    path('post-gps', views.GPSView.as_view()),
    path('get-corner-cords', views.CornerCordsView.as_view()),
    path('post-corner-cords', views.CornerCordsView.as_view()),
    path('get-nodes', views.NodeView.as_view()),
    path('post-nodes', views.NodeView.as_view()),
]