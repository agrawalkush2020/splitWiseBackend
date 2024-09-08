from django.urls import path
from groups import views

urlpatterns = [
    path('', views.get_group_list),
    path('make_group/',views.make_group),
]
