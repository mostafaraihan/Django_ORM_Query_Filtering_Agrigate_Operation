from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.home),
    path('fetch_alldata/', views.fetch_alldata),
    path('fetch_singledata/', views.fetch_singledata),
]