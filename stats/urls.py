from django.urls import path
from stats import views

urlpatterns = [
    path('fetch/', views.fetch_app_stats)
]
