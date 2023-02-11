from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.doctor_home, name="doctor_home"),
    path('signup/', views.d_signup, name="d_signup"),
    path('signin/', views.d_signin, name="d_signin"),
    path('signout/', views.d_signout, name="d_signout"),
    path('add-profile/', views.add_doctor_profile, name="add_doctor_profile"),
    path('view-profile/', views.view_doctor_profile, name="view_doctor_profile"),
]