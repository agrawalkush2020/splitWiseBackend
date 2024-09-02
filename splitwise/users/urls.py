from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('signup/', views.handle_signup),
    path('login/', views.handle_login)
]
