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
    path('limiting_data/', views.limiting_data),
    path('count_data/', views.count_data),
    path('max_data/', views.max_data),
    path('min_data/', views.min_data),
    path('avg_data/', views.avg_data),
    path('sum_data/', views.sum_data),
    path('aggregate_data/', views.aggregate_data),
    path('insert_data/', views.insert_data),
    path('insert_multiple_data/', views.insert_multiple_data),
    path('delete_data/', views.delete_data),
    path('update_data/', views.update_data),
]
