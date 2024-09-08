from django.urls import path
from transactions import views

urlpatterns = [
    path('fetch_all_transactions/', views.fetch_all_transactions),
    path('fetch_all_transactions_by_gid/', views.fetch_all_transactions_by_gid),

]
