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
    path('view-my-bookings/', views.view_my_bookings, name="view_my_bookings"),
    path('view-doctor-profile/<int:id>', views.view_doctor_profile, name="view_doctor_profile"),
    path('book-doctor/<int:id>', views.book_doctor, name="book_doctor"),
    path('add-vaccine/', views.add_vaccine, name="add_vaccine"),
    path('view-my-vaccines/', views.view_my_vaccines, name="view_my_vaccines"),
]