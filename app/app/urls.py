from django.urls import path
from . import views

urlpatterns = [
    path("cctv/", views.cctv),
    path("lamp/", views.lamp),
    path("accident/", views.accident),
    path("sidewalk/", views.sidewalk),
    path("sidewalk_point/", views.sidewalk_point),
]
