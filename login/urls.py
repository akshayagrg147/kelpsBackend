from django.urls import path
from . import views

urlpatterns = [
    path('user_login', views.user_login),
    path('user_register', views.user_register),
    path('user_info', views.user_info),
    path('gst_verification', views.gst_verification)
]
