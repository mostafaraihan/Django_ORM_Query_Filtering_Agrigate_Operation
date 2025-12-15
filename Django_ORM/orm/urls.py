from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.home),
    path('fetch_alldata/', views.fetch_alldata),
    path('fetch_singledata/', views.fetch_singledata),
    path('fetch_firstdata/', views.fetch_firstdata),
    path('fetch_lastdata/', views.fetch_lastdata),
    path('filter_data/', views.filter_data),
    path('exclude_data/', views.exclude_data),
    path('sort_ascending/', views.sort_ascending),
    path('sort_descending/', views.sort_descending),
]