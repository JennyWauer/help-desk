from django.urls import path

from . import views

urlpatterns = [
    path('', views.about),
    path('login/', views.login),
    path('register/', views.register),
    path('new_user/', views.new_user),
    path('home/', views.home),
]