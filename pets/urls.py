from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.pet_home, name="pet_home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('add-profile/', views.add_user_profile, name="add_user_profile"),
    path('view-profile/', views.view_user_profile, name="view_user_profile"),
    path('view-all-doctors/', views.view_all_doctors, name="view_all_doctors"),
    path('view-doctor-profile/<int:id>', views.view_doctor_profile, name="view_doctor_profile"),
]