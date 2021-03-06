from django.urls import path

from . import views

urlpatterns = [
    path('', views.about),
    path('login/', views.login),
    path('register/', views.register),
    path('new_user/', views.new_user),
    path('home/', views.home),
    path('new_ticket/', views.new_ticket),
    path('create_ticket/', views.create_ticket),
    path('user_login/', views.user_login),
    path('<int:user_id>/', views.profile),
]