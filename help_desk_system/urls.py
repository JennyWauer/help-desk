from django.urls import path

from . import views

urlpatterns = [
    path('', views.about),
    path('login/', views.login),
    path('register/', views.register),
]